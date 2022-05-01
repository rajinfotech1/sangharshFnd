from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    mobile_nomber = models.BigIntegerField()
    alternet_mobile_nomber = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='profile')
    address = models.TextField(blank=True, null=True)
     
    AP = "A+"
    AM = "A-"
    BP = "B+"
    BM = "B-"
    ABP = "AB+"
    ABM = "AB-"
    OP = "O+"
    OM = "O-"
    
    BLOOD_GROUP_CHOICES = [
        (AP, "A+"),
        (AM,"A-"),
        (BP, "B+"),
        (BM, "B-"),
        (ABP, "AB+"),
        (ABM, "AB-"),
        (OP,"O+"),
        (OM, "O-"),
    ]
    
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    
    is_member = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = CustomUserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    