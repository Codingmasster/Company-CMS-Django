from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_CHOICES = (
        (1, 'Head'),
        (2, 'Employee'),
    )
    
    BLOOD_GROUP_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

    user_type = models.CharField(choices=USER_CHOICES, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)  # Changed from last_names
    date_joined = models.DateField(auto_now_add=True)
    cnic = models.CharField(max_length=15)
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES, max_length=3)  # Changed from bg
    address = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to='profile_pics/')  # Changed upload_to path
    cv = models.FileField(upload_to='cvs/')
    email = models.EmailField(blank=True)
    phone_no = models.CharField(max_length=20,blank=True)
    dob = models.DateField(blank=True,null=True)  # Changed upload_to path
