from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.book_travel, name='book_travel'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.update_profile, name='profile'),
    path('signup/', views.signup_view, name='signup'),

]
