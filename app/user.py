from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        # Add more choices if needed
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default='patient', max_length=10)
    # Add other fields as needed for each type of user
