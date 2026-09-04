from django.core.management.base import BaseCommand
from core.models import Worker

class Command(BaseCommand):
    help = 'Create demo cooperative workers'
    def handle(self, *args, **kwargs):
        data = [
            ('Ramesh Kumar','Plumbing','Vijay Nagar',8,4.8,2),
            ('Suresh Verma','Plumbing','Palasia',5,4.6,5),
            ('Amit Sharma','Electrical','Vijay Nagar',7,4.9,7),
            ('Neha Patel','Cleaning','Palasia',4,4.7,3),
            ('Mohan Singh','Carpentry','Rau',9,4.5,1),
            ('Pooja Joshi','Painting','Bhawarkua',6,4.8,4),
        ]
        for name, service, area, exp, rating, jobs in data:
            Worker.objects.get_or_create(name=name, defaults={'service':service,'area':area,'experience':exp,'rating':rating,'recent_jobs':jobs,'verified':True,'availability':True})
        self.stdout.write(self.style.SUCCESS('Demo workers ready.'))
