from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db import models

class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SELLER = "SELLER", "Seller"
    BUYER = "BUYER", "Buyer"
    USER = "USER", "User"

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('role', Role.USER)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', Role.ADMIN)
        
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self) :
        return self.email