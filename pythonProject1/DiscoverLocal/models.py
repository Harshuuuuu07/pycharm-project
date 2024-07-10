from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

class user(models.Model):
    NAME = models.CharField(max_length=50)
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField()
    PASSWORD = models.IntegerField()
    def __str__(self):
        return self.NAME
class Country(models.Model):
    Country_NAME = models.CharField(max_length=25)

    def __str__(self):
        return self.Country_NAME

class state(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    State_NAME = models.CharField(max_length=25)
    def __str__(self):
        return self.State_NAME
class city(models.Model):
    State_NAME = models.ForeignKey(state, on_delete=models.CASCADE)
    city_NAME = models.CharField(max_length=25)
    def __str__(self):
        return self.city_NAME
class EventCategory(models.Model):
    name = models.CharField(max_length=25)
    Description = models.TextField()
    def __str__(self):
        return self.name
class Event(models.Model):
    TITLE = models.CharField(max_length=25)
    DESCRIPTION = models.TextField()
    CATEGORY = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    VENUE_NAME = models.CharField(max_length=25)
    ADDRESS =  models.TextField()
    CITY = models.ForeignKey(city, on_delete=models.CASCADE)
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    Booking_from = models.DateField()
    Booking_To = models.DateField()
    CREATED_AT = models.DateField(default=timezone.now)
    def __str__(self):
        return self.TITLE
class Booking(models.Model):
    STATUS = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
        ]
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    Booking = models.ForeignKey(Event, on_delete=models.CASCADE)
    Booking_date = models.DateField()
    Status = models.CharField(max_length=25, choices=STATUS, default='pending')
    def __str__(self):
        return self.user.NAME
class Payment(models.Model):
    Payment = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Credit card', 'Credit card'),
        ('Debit card', 'Debit card'),
        ('Digital wallet', 'Digital wallet'),
    ]
    STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]
    BOOKING = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=25, choices=Payment)
    Payment_date = models.DateField()
    payment_status = models.CharField(max_length=25, choices=STATUS)
    def __str__(self):
        return self.BOOKING.user.NAME
class Feedback(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Comment = models.TextField()
    Review_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.NAME
class Contactus(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(verbose_name='Email')
    Phone = models.BigIntegerField()
    Message = models.TextField()
    Created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Name
