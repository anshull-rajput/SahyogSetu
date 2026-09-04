from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=1)
    rating = models.FloatField(default=4.5)
    recent_jobs = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(default=True)
    availability = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True)
    cooperative = models.CharField(max_length=150, default='Sahyog Labour Cooperative')

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS = [('pending','Pending'),('accepted','Accepted'),('rejected','Rejected'),('completed','Completed')]
    customer_name = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    rating = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} - {self.customer_name}'
