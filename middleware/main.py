from django.shortcuts import redirect
from django.urls import reverse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
    
        # Check if the user is authenticated
        if request.user.is_authenticated:
            user_role = request.user.role
            request_path = request.path

            # Redirect logged-in users based on their role
            if user_role == "ADMIN" and request_path.startswith("/seller/"):
                return redirect(reverse("events:events"))
            elif user_role == "ADMIN" and request_path.startswith("/buyer/"):
                return redirect(reverse("events:events"))

            if user_role == "SELLER" and request_path.startswith("/admin/"):
                return redirect(reverse("events:sellers"))
            elif user_role == "SELLER" and request_path.startswith("/buyer/"):
                return redirect(reverse("events:sellers"))

            if user_role == "BUYER" and request_path.startswith("/admin/"):
                return redirect(reverse("events:buyers"))
            elif user_role == "BUYER" and request_path.startswith("/seller/"):
                return redirect(reverse("events:buyers"))

        else:
            # Redirect unauthenticated users trying to access protected routes
            if request.path.startswith("/admin/") or request.path.startswith("/seller/") or request.path.startswith("/buyer/"):
                return redirect(reverse("account:login"))

        return self.get_response(request)