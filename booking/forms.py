from django import forms
from .models import Booking
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_seats']
        def __init__(self, *args, **kwargs):
            self.travel_option = kwargs.pop('travel_option', None)
            super().__init__(*args, **kwargs)

    def clean_number_of_seats(self):
        seats = self.cleaned_data['number_of_seats']
        if self.travel_option and seats > self.travel_option.available_seats:
            raise forms.ValidationError(
                f"Only {self.travel_option.available_seats} seats are available."
            )
        return seats
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
