from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('book/<int:worker_id>/', views.book, name='book'),
    path('customer/', views.customer_bookings, name='customer_bookings'),
    path('worker/', views.worker_dashboard, name='worker_dashboard'),
    path('booking/<int:booking_id>/<str:action>/', views.update_booking, name='update_booking'),
    path('rate/<int:booking_id>/', views.rate_booking, name='rate_booking'),
    path('cooperative/', views.coop_dashboard, name='coop_dashboard'),
]
