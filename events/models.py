from django.db import models
from django.conf import settings

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    event_time = models.DateTimeField()
    seller_invite_code = models.CharField(max_length=100)
    buyer_invite_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class EventEnrollment(models.Model):
    id = models.AutoField(primary_key=True)
    invite_code = models.CharField(max_length=100)
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="enrollments")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="event_enrollments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"Enrollment for {self.event.name} by {self.user.username}"

class BookingSlot(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event', related_name='booking_slots', on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slot for {self.event.name} at {self.booking_time}"
