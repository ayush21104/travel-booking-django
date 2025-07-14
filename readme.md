Travel Booking Django Application A simple web-based travel booking system built using Django, where users can browse available travel options, make bookings, and manage their reservations.

Features User Registration, Login, Logout

View available travel options (Flight, Train, Bus)

Filtered booking system with price, seat count, and travel date

Booking form with seat validation

Live seat deduction on successful booking

View and manage your bookings

Cancel bookings (with optional seat restore logic)

Admin dashboard for managing travel data

Tech Stack Backend: Django (Python)

Frontend: Django Templates + HTML/CSS (Bootstrap optional)

Database: SQLite (easily replaceable with MySQL)

Authentication: Django’s built-in auth system

Project Structure bash Copy code travel_booking/ ├── booking/ # Core app │ ├── models.py │ ├── views.py │ ├── urls.py │ ├── forms.py │ └── templates/booking/ ├── templates/registration/ # Login/Signup pages ├── static/ # CSS or Bootstrap ├── manage.py └── travel_booking/ # Main settings + URLs ⚙️ Setup Instructions Clone the repository:

bash Copy code git clone https://github.com/ayush21104/travel-booking-django.git cd travel-booking-django Set up a virtual environment:

bash Copy code python -m venv env source env/bin/activate # On Windows: env\Scripts\activate Install dependencies:

bash Copy code pip install -r requirements.txt Run migrations:

bash Copy code python manage.py makemigrations python manage.py migrate Create a superuser:

bash Copy code python manage.py createsuperuser Run the development server:

bash Copy code python manage.py runserver Visit http://127.0.0.1:8000/ to access the app.