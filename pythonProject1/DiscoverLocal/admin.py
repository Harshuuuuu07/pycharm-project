from django.contrib import admin
from .models import *
# Register your models here.
class showuser(admin.ModelAdmin):
    list_display = ['NAME', 'FIRST_NAME', 'LAST_NAME',  'EMAIL', 'PASSWORD']
class showCountry(admin.ModelAdmin):
    list_display = ['Country_NAME']
class showstate(admin.ModelAdmin):
    list_display = ['State_NAME', 'Country']
class showcity(admin.ModelAdmin):
    list_display = ['State_NAME', 'city_NAME']
class showEventCategory(admin.ModelAdmin):
    list_display = ['name', 'Description']
class showEvent(admin.ModelAdmin):
    list_display = ['TITLE', 'DESCRIPTION', 'CATEGORY', 'VENUE_NAME', 'ADDRESS', 'CITY', 'state', 'Country', 'Booking_from', 'Booking_To', 'CREATED_AT']
class showBooking(admin.ModelAdmin):
    list_display = ['user', 'Booking', 'Booking_date', 'Status']
class showPayment(admin.ModelAdmin):
    list_display = ['BOOKING', 'Event', 'payment_mode', 'payment_status', 'Payment_date']
class showFeedback(admin.ModelAdmin):
    list_display = ['user', 'event', 'Rating', 'Comment', 'Review_date']
class showContactus(admin.ModelAdmin):
            list_display = ['Name', 'Email', 'Phone', 'Message', 'Created_at']
admin.site.register(user, showuser)
admin.site.register(Country, showCountry)
admin.site.register(state, showstate)
admin.site.register(city, showcity)
admin.site.register(EventCategory, showEventCategory)
admin.site.register(Event, showEvent)
admin.site.register(Booking, showBooking)
admin.site.register(Payment, showPayment)
admin.site.register(Feedback, showFeedback)
admin.site.register(Contactus, showContactus)