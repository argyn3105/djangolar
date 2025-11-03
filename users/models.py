
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """User model extending AbstractUser"""
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils import timezone

# class CustomAccount(AbstractBaseUser, PermissionsMixin):
#     """User model using AbstractBaseUser"""
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=150)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name']

#     def __str__(self):
#         return self.email
