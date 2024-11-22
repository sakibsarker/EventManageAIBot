from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from .models import Event
from django.views import View
import random
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views import View
import os
from dotenv import load_dotenv
from langchain_fireworks import ChatFireworks
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ["FIREWORKS_API_KEY"] = os.getenv("FIREWORK_API_KEY")

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
class EventDeleteView(View):
    def post(sel,request,event_id):
        event=get_object_or_404(Event,id=event_id)
        event.delete()
        return redirect('events:events')

class ChatBotView(TemplateView):
    template_name = 'chatbot/chat.html'

class GenerateResponseView(View):
    def post(self, request, *args, **kwargs):
        user_input = request.POST.get('user_input', '')
        
        if user_input:
            try:
                # Initialize model and template
                model = ChatFireworks(model="accounts/fireworks/models/llama-v3p1-70b-instruct")
                
                chat_template = ChatPromptTemplate.from_messages([
                    ("system", "You are a helpful assistant that writes concise 50-word descriptions."),
                    ("user", "Write a 50-word description about {user_input}"),
                ])
                
                # Create chain and generate response
                chain = chat_template | model
                response = chain.invoke({"user_input": user_input})
                
                return JsonResponse({
                    'status': 'success',
                    'response': response.content
                })
            except Exception as e:
                return JsonResponse({
                    'status': 'error',
                    'message': str(e)
                }, status=500)
        
        return JsonResponse({
            'status': 'error',
            'message': 'No input provided'
        }, status=400)