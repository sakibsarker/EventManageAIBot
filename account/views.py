from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser  # Import the CustomUser model
# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, "auth/login.html")
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect("/events/")
        else:
            return render(request,"auth/login.html",{"error":"Invalid email or password."})

class SignUpView(View):
    def get(self, request):
        return render(request, "auth/signup.html")

    def post(self, request):
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        company = request.POST.get('company')
        services = request.POST.get('services')
        role = request.POST.get('role')

        # Create a new user
        user = CustomUser(
            name=name,
            email=email,
            phone=phone,
            company=company,
            services=services,
            role=role
        )
        user.set_password(password)  # Set the password
        user.save()  # Save the user to the database

        return redirect('/')  # Redirect to a success page or home

class LogoutView(View):
    def post(self,request):
        logout(request)
        return redirect('/')
    
