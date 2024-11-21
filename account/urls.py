from django.urls import path
from . import views
app_name = "account"
urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("signup/",views.SignUpView.as_view(), name="Signup"),
    path("logout/",views.LogoutView.as_view(),name='Logout'),

]