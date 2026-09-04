from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)
    login_username = models.CharField(max_length=50, unique=True, default='worker')
    service = models.CharField(max_length=50)
    skills = models.TextField(default='', blank=True)
    area = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=1)
    rating = models.FloatField(default=4.5)
    recent_jobs = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(default=True)
    availability = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True)
    cooperative = models.CharField(max_length=150, default='Sahyog Labour Cooperative')
    member_id = models.CharField(max_length=30, default='COOP1000')
    welfare_health = models.BooleanField(default=True)
    welfare_accident = models.BooleanField(default=True)

    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS = [
        ('pending', 'Pending Worker Approval'),
        ('accepted', 'Confirmed'),
        ('progress', 'Service In Progress'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    customer_name = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    estimated_cost = models.PositiveIntegerField(default=450)
    payment_status = models.CharField(max_length=20, default='unpaid')
    transaction_id = models.CharField(max_length=40, blank=True)
    review = models.TextField(blank=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(choices=STATUS, default='pending', max_length=20)
    rating = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} - {self.customer_name}'
