from django.contrib import admin
from .models import Booking, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'area', 'rating', 'recent_jobs', 'verified', 'availability', 'member_id')
    list_filter = ('service', 'verified', 'availability')
    search_fields = ('name', 'area', 'skills', 'member_id')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'customer_name', 'worker', 'status', 'estimated_cost', 'payment_status', 'rating')
    list_filter = ('status', 'service', 'payment_status')
    search_fields = ('customer_name', 'worker__name')
