from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.type})"
