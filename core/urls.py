from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('search/', views.search, name='search'),
    path('book/<int:worker_id>/', views.book, name='book'),
    path('bookings/', views.customer_bookings, name='customer_bookings'),
    path('booking/<int:booking_id>/<str:action>/', views.update_booking, name='update_booking'),
    path('booking/<int:booking_id>/pay/', views.pay_booking, name='pay_booking'),
    path('booking/<int:booking_id>/rate/', views.rate_booking, name='rate_booking'),
    path('worker/', views.worker_dashboard, name='worker_dashboard'),
    path('cooperative/', views.coop_dashboard, name='coop_dashboard'),
    path('cooperative/worker/<int:worker_id>/', views.worker_profile, name='worker_profile'),
    path('cooperative/worker/<int:worker_id>/<str:action>/', views.verify_worker, name='verify_worker'),
]
