from django.urls import path
from . import views
app_name = "events"
urlpatterns = [
    path("admin/", views.EvenView.as_view(), name="events"),
    path("admin/event/create/", views.EventCreateView.as_view(), name="createevent"),
    path("admin/<int:event_id>/event", views.EventDetailsView.as_view(), name="event_detail"),
    path("admin/<int:event_id>/delete/", views.EventDeleteView.as_view(), name="delete_event"),
    path("admin/profile/", views.AdminProfileView.as_view(), name="admin_profile"),
    path("admin/chat/", views.ChatBotView.as_view(), name="chatbot"),
    path('admin/generate/',views.GenerateResponseView.as_view(), name='generate_response'),
    path("seller/", views.SellerDashboard.as_view(), name="sellers"),
    path("buyer/", views.BuyerDashboard.as_view(), name="buyers"),
 
]