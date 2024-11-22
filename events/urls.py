from django.urls import path
from . import views
app_name = "events"
urlpatterns = [
    path("admin/", views.EvenView.as_view(), name="events"),
    path("create/admin/", views.EventCreateView.as_view(), name="createevent"),
    path("<int:event_id>/admin/", views.EventDetailsView.as_view(), name="event_detail"),
    path("<int:event_id>/delete/admin/", views.EventDeleteView.as_view(), name="delete_event"),
    path("chat/", views.ChatBotView.as_view(), name="chatbot"),
    path('generate/',views.GenerateResponseView.as_view(), name='generate_response'),
 
]