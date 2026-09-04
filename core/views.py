from django.shortcuts import get_object_or_404, redirect, render
from .models import Booking, Worker

SERVICES = ['Plumbing','Electrical','Carpentry','Cleaning','Painting','Gardening','Driving','Caregiving','Technician']

AREA_SCORE = {'Vijay Nagar': 15, 'Palasia': 13, 'Bhawarkua': 11, 'Rau': 9, 'Indore': 8}

def home(request):
    return render(request, 'home.html', {'services': SERVICES})

def match_score(worker, area):
    skill = 40
    availability = 20 if worker.availability else 0
    distance = AREA_SCORE.get(worker.area, 7) if worker.area.lower() == area.lower() else 5
    rating = round((worker.rating / 5) * 15)
    fairness = max(0, 10 - min(worker.recent_jobs, 10))
    return skill + availability + distance + rating + fairness

def search(request):
    service = request.GET.get('service','Plumbing')
    area = request.GET.get('area','Indore')
    date = request.GET.get('date','')
    time = request.GET.get('time','')
    workers = [w for w in Worker.objects.all() if w.service.lower() == service.lower() and w.availability and w.verified]
    ranked = sorted([(w, match_score(w, area)) for w in workers], key=lambda x: x[1], reverse=True)
    return render(request, 'search.html', {'workers': ranked, 'service': service, 'area': area, 'date': date, 'time': time})

def book(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if request.method == 'POST':
        Booking.objects.create(customer_name=request.POST.get('customer_name','Demo Customer'), service=worker.service, area=request.POST.get('area', worker.area), date=request.POST.get('date',''), time=request.POST.get('time',''), worker=worker)
        return redirect('customer_bookings')
    return render(request, 'book.html', {'worker': worker})

def customer_bookings(request):
    bookings = Booking.objects.all().order_by('-created_at')[:20]
    return render(request, 'customer.html', {'bookings': bookings})

def worker_dashboard(request):
    bookings = Booking.objects.filter(status__in=['pending','accepted']).order_by('-created_at')
    return render(request, 'worker.html', {'bookings': bookings})

def update_booking(request, booking_id, action):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = {'accept':'accepted','reject':'rejected','complete':'completed'}.get(action, booking.status)
    booking.save()
    if booking.status == 'completed':
        booking.worker.recent_jobs += 1
        booking.worker.save(update_fields=['recent_jobs'])
    return redirect('worker_dashboard')

def rate_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST' and booking.status == 'completed':
        booking.rating = int(request.POST.get('rating',5))
        booking.save(update_fields=['rating'])
    return redirect('customer_bookings')

def coop_dashboard(request):
    workers = Worker.objects.all()
    bookings = Booking.objects.all()
    context = {'workers': workers, 'bookings': bookings, 'total_workers': workers.count(), 'verified_workers': workers.filter(verified=True).count(), 'active': bookings.filter(status__in=['pending','accepted']).count(), 'completed': bookings.filter(status='completed').count()}
    return render(request, 'admin_dashboard.html', context)
