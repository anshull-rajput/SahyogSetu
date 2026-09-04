from functools import wraps
from random import randint

from django.contrib import messages
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render

from .models import Booking, Worker

SERVICES = ['Plumbing', 'Electrical', 'Cleaning', 'Carpentry', 'Painting', 'Gardening', 'Caregiving', 'Driving', 'Technician']
SERVICE_COSTS = {'Plumbing': 450, 'Electrical': 500, 'Cleaning': 350, 'Carpentry': 650, 'Painting': 700, 'Gardening': 400, 'Caregiving': 600, 'Driving': 550, 'Technician': 550}
DEMO_CUSTOMERS = ['Rahul', 'Priya', 'Arjun']
AREAS = ['Vijay Nagar', 'Palasia', 'Rau', 'Rajendra Nagar', 'Bhanwarkuan', 'Scheme No. 54']


def role_required(role):
    def decorator(view):
        @wraps(view)
        def wrapped(request, *args, **kwargs):
            if request.session.get('role') != role:
                return redirect('login')
            return view(request, *args, **kwargs)
        return wrapped
    return decorator


def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role', 'customer')
        request.session['role'] = role
        request.session['customer_name'] = request.POST.get('customer_name', 'Rahul')
        if role == 'worker':
            request.session['worker_id'] = int(request.POST.get('worker_id') or Worker.objects.filter(verified=True).first().id)
            return redirect('worker_dashboard')
        if role == 'admin':
            return redirect('coop_dashboard')
        return redirect('customer_dashboard')
    workers = Worker.objects.filter(verified=True).order_by('name')
    return render(request, 'login.html', {'workers': workers, 'customers': DEMO_CUSTOMERS})


def logout_view(request):
    request.session.flush()
    return redirect('login')


def home(request):
    if request.session.get('role') == 'customer':
        return redirect('customer_dashboard')
    return render(request, 'home.html', {'services': SERVICES})


@role_required('customer')
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html', {'services': SERVICES, 'areas': AREAS})


def distance_score(worker_area, customer_area):
    if worker_area.lower().strip() == customer_area.lower().strip():
        return 15, 'Nearby'
    close = {('vijay nagar', 'scheme no. 54'), ('scheme no. 54', 'vijay nagar'), ('palasia', 'vijay nagar'), ('vijay nagar', 'palasia'), ('ra u', 'rajendra nagar')}
    pair = (worker_area.lower().strip(), customer_area.lower().strip())
    return (11, 'Short distance') if pair in close else (6, 'Farther away')


def match_score(worker, area):
    location_points, _ = distance_score(worker.area, area)
    availability = 20 if worker.availability else 0
    rating = round((min(worker.rating, 5) / 5) * 15)
    fairness = max(0, 10 - min(worker.recent_jobs, 10))
    return 40 + availability + location_points + rating + fairness


def recommendation_reason(worker, area):
    _, distance_label = distance_score(worker.area, area)
    reasons = ['Skill matches', 'Verified cooperative member']
    if worker.availability:
        reasons.append('Available')
    reasons.append(distance_label)
    if worker.recent_jobs <= 5:
        reasons.append('Lower recent workload')
    return reasons


@role_required('customer')
def search(request):
    service = request.GET.get('service', 'Plumbing')
    area = request.GET.get('area', 'Vijay Nagar')
    date = request.GET.get('date', '')
    time = request.GET.get('time', '')
    description = request.GET.get('description', '')
    workers = Worker.objects.filter(verified=True, availability=True, service__iexact=service)
    ranked = []
    for worker in workers:
        score = match_score(worker, area)
        ranked.append((worker, score, recommendation_reason(worker, area)))
    ranked.sort(key=lambda item: item[1], reverse=True)
    return render(request, 'search.html', {'workers': ranked, 'service': service, 'area': area, 'date': date, 'time': time, 'description': description, 'areas': AREAS})


@role_required('customer')
def book(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id, verified=True)
    if request.method == 'POST':
        Booking.objects.create(
            customer_name=request.session.get('customer_name', 'Rahul'),
            service=worker.service,
            area=request.POST.get('area', worker.area),
            date=request.POST.get('date', ''),
            time=request.POST.get('time', ''),
            description=request.POST.get('description', ''),
            estimated_cost=SERVICE_COSTS.get(worker.service, 450),
            worker=worker,
        )
        messages.success(request, f'Booking request sent to {worker.name}.')
        return redirect('customer_bookings')
    return render(request, 'book.html', {'worker': worker, 'areas': AREAS, 'cost': SERVICE_COSTS.get(worker.service, 450)})


@role_required('customer')
def customer_bookings(request):
    customer = request.session.get('customer_name', 'Rahul')
    bookings = Booking.objects.filter(customer_name=customer).select_related('worker').order_by('-created_at')
    return render(request, 'customer.html', {'bookings': bookings, 'customer': customer})


@role_required('customer')
def pay_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer_name=request.session.get('customer_name'))
    if request.method == 'POST' and booking.status == 'completed':
        booking.payment_status = 'paid'
        booking.transaction_id = f'TXN{booking.id:04d}{randint(10, 99)}'
        booking.save(update_fields=['payment_status', 'transaction_id'])
        messages.success(request, f'Payment successful. Transaction ID: {booking.transaction_id}')
    return redirect('customer_bookings')


@role_required('customer')
def rate_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer_name=request.session.get('customer_name'))
    if request.method == 'POST' and booking.status == 'completed':
        booking.rating = max(1, min(5, int(request.POST.get('rating', 5))))
        booking.review = request.POST.get('review', '').strip()
        booking.save(update_fields=['rating', 'review'])
        avg = booking.worker.bookings.filter(rating__isnull=False).aggregate(avg=Avg('rating'))['avg']
        if avg is not None:
            booking.worker.rating = round(avg, 2)
            booking.worker.save(update_fields=['rating'])
        messages.success(request, 'Thanks! Your rating has been recorded.')
    return redirect('customer_bookings')


@role_required('worker')
def worker_dashboard(request):
    worker = get_object_or_404(Worker, id=request.session.get('worker_id'))
    bookings = worker.bookings.select_related('worker').order_by('-created_at')
    completed = bookings.filter(status='completed')
    earnings = sum(b.estimated_cost for b in completed)
    return render(request, 'worker.html', {'worker': worker, 'bookings': bookings, 'earnings': earnings, 'completed_count': completed.count()})


@role_required('worker')
def update_booking(request, booking_id, action):
    worker = get_object_or_404(Worker, id=request.session.get('worker_id'))
    booking = get_object_or_404(Booking, id=booking_id, worker=worker)
    if request.method == 'POST':
        new_status = {'accept': 'accepted', 'reject': 'rejected', 'progress': 'progress', 'complete': 'completed'}.get(action)
        if new_status and ((booking.status == 'pending' and action in ['accept', 'reject']) or (booking.status == 'accepted' and action == 'progress') or (booking.status == 'progress' and action == 'complete')):
            booking.status = new_status
            booking.save(update_fields=['status'])
            if new_status == 'completed':
                worker.recent_jobs += 1
                worker.save(update_fields=['recent_jobs'])
            messages.success(request, f'Booking {booking.id} updated to {booking.get_status_display()}.')
    return redirect('worker_dashboard')


@role_required('admin')
def coop_dashboard(request):
    workers = Worker.objects.all().order_by('-verified', 'name')
    bookings = Booking.objects.select_related('worker').order_by('-created_at')
    stats = {
        'total_workers': workers.count(),
        'verified_workers': workers.filter(verified=True).count(),
        'pending_workers': workers.filter(verified=False).count(),
        'active': bookings.filter(status__in=['pending', 'accepted', 'progress']).count(),
        'completed': bookings.filter(status='completed').count(),
    }
    service_stats = list(bookings.values('service').annotate(total=Count('id')).order_by('-total'))
    return render(request, 'admin_dashboard.html', {'workers': workers, 'bookings': bookings, 'stats': stats, 'service_stats': service_stats})


@role_required('admin')
def verify_worker(request, worker_id, action):
    worker = get_object_or_404(Worker, id=worker_id)
    if request.method == 'POST':
        worker.verified = action == 'approve'
        worker.save(update_fields=['verified'])
        messages.success(request, f'{worker.name} verification updated.')
    return redirect('coop_dashboard')


@role_required('admin')
def worker_profile(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    return render(request, 'worker_profile.html', {'worker': worker})
