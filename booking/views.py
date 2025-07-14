from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from .forms import BookingForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

def home(request):
    travel_options = TravelOption.objects.all()
    return render(request, 'booking/travel_list.html', {'travel_options': travel_options})

@login_required
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.num_seats > travel.available_seats:
                messages.error(request, "Not enough seats available.")
                return redirect('home')
            booking.user = request.user
            booking.travel_option = travel
            booking.total_price = travel.price * booking.num_seats
            travel.available_seats -= booking.num_seats
            travel.save()
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form, 'travel': travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != 'Cancelled':
        booking.status = 'Cancelled'
        booking.travel_option.available_seats += booking.num_seats
        booking.travel_option.save()
        booking.save()
    return redirect('my_bookings')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'booking/profile.html', {'form': form})

from .forms import SignupForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after signup
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
