from django.core.management.base import BaseCommand
from core.models import Worker, Booking


class Command(BaseCommand):
    help = 'Create demo cooperative workers and bookings'

    def handle(self, *args, **kwargs):
        Worker.objects.all().delete()
        workers = [
            ('Rajesh Kumar','Plumbing','Pipe repair, Bathroom plumbing, Water tank installation','Vijay Nagar',6,4.8,3,True,True,'9876500001','COOP1001'),
            ('Suresh Verma','Plumbing','Pipe repair, Leakage fixing','Palasia',5,4.6,8,True,True,'9876500002','COOP1002'),
            ('Mohan Singh','Plumbing','Bathroom plumbing, Fittings','Rau',9,4.5,1,True,True,'9876500003','COOP1003'),
            ('Amit Sharma','Electrical','Wiring, Fan repair, Switch installation','Vijay Nagar',7,4.9,9,True,True,'9876500004','COOP1004'),
            ('Vikram Patel','Electrical','Wiring, Appliance repair','Rajendra Nagar',4,4.7,4,True,True,'9876500005','COOP1005'),
            ('Neha Patel','Cleaning','Home cleaning, Deep cleaning, Kitchen cleaning','Palasia',4,4.7,3,True,True,'9876500006','COOP1006'),
            ('Sunita Joshi','Cleaning','Home cleaning, Bathroom cleaning','Rau',6,4.6,6,False,True,'9876500007','COOP1007'),
            ('Karan Yadav','Carpentry','Furniture repair, Door fitting','Bhanwarkuan',8,4.5,2,True,True,'9876500008','COOP1008'),
            ('Pooja Joshi','Painting','Wall painting, Touch-up, Texture','Scheme No. 54',6,4.8,4,True,True,'9876500009','COOP1009'),
            ('Deepak Rao','Gardening','Garden maintenance, Plant care','Rajendra Nagar',5,4.4,7,True,True,'9876500010','COOP1010'),
            ('Meena Sharma','Caregiving','Elder care, Daily assistance','Vijay Nagar',7,4.9,2,True,True,'9876500011','COOP1011'),
            ('Arun Das','Driving','Local driving, Errands','Palasia',10,4.6,5,True,True,'9876500012','COOP1012'),
            ('Ravi Kumar','Technician','Appliance repair, AC service','Bhanwarkuan',6,4.3,10,True,True,'9876500013','COOP1013'),
            ('Sunil Jain','Electrical','Inverter repair, Wiring','Rau',5,4.2,12,True,True,'9876500014','COOP1014'),
            ('Anita Verma','Cleaning','Deep cleaning, Move-in cleaning','Scheme No. 54',3,4.5,1,True,True,'9876500015','COOP1015'),
        ]
        for name, service, skills, area, exp, rating, jobs, verified, available, phone, member_id in workers:
            Worker.objects.create(name=name, service=service, skills=skills, area=area, experience=exp, rating=rating, recent_jobs=jobs, verified=verified, availability=available, phone=phone, member_id=member_id)
        rajesh = Worker.objects.get(member_id='COOP1001')
        amit = Worker.objects.get(member_id='COOP1004')
        neha = Worker.objects.get(member_id='COOP1006')
        Booking.objects.all().delete()
        Booking.objects.create(customer_name='Rahul', service='Plumbing', area='Vijay Nagar', date='05/09/2026', time='16:00', description='Kitchen sink pipe is leaking.', estimated_cost=450, worker=rajesh, status='pending')
        Booking.objects.create(customer_name='Priya', service='Electrical', area='Vijay Nagar', date='05/09/2026', time='11:00', description='Ceiling fan needs repair.', estimated_cost=500, worker=amit, status='accepted')
        Booking.objects.create(customer_name='Arjun', service='Cleaning', area='Palasia', date='03/09/2026', time='10:00', description='Deep cleaning required.', estimated_cost=350, worker=neha, status='completed', rating=5, review='Very professional and on time.', payment_status='paid', transaction_id='TXNDEMO1003')
        Booking.objects.create(customer_name='Rahul', service='Plumbing', area='Rau', date='02/09/2026', time='15:00', description='Tap replacement.', estimated_cost=450, worker=Worker.objects.get(member_id='COOP1003'), status='rejected')
        self.stdout.write(self.style.SUCCESS('Demo cooperative data ready.'))
