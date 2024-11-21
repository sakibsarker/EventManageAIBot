from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Event
from django.views import View
import random


def generate_invite_code():
    return f"{random.randint(100000, 999999)}"

class EventCreateView(View):
    def get(self,request):
        return render(request,"admin/createevent.html")
    def post(self,request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        event_time = request.POST.get("event_time")
        seller_invite_code = generate_invite_code()
        buyer_invite_code = generate_invite_code()
        event=Event.objects.create(
            name=name,
            description=description,
            event_time=event_time,
            seller_invite_code=seller_invite_code,
            buyer_invite_code=buyer_invite_code
        )
        return HttpResponse(f"Event created successfully: {event.name} (Seller: {seller_invite_code}, Buyer: {buyer_invite_code})")

class EvenView(View):
    def get(self,request):
        events=Event.objects.all()
        return render(request,"admin/allevent.html",{'events':events})
    

class EventDetailsView(View):
    def get(self,request, event_id):
        event=get_object_or_404(Event,id=event_id)
        return render(request,"admin/eventdetails.html",{"event": event})
    
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        
        # Get updated data from the form
        name = request.POST.get("name")
        description = request.POST.get("description")
        event_time = request.POST.get("event_time")
        
        # Update event with new data
        event.name = name
        event.description = description
        event.event_time = event_time
        event.save()  # Save the updated event
        
        # Optionally, send a response to inform the user of the update
        return HttpResponse(f"Event updated successfully: {event.name}")