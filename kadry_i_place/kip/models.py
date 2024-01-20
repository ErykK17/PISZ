from django.db import models
from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user')
    user_type = models.CharField(
        max_length=10,
        choices=[
            ('kierownik', 'Kierownik'),
            ('pracownik', 'Pracownik')
        ]
    )
    phone_number = models.IntegerField(null=True, blank=True)
    pesel = models.IntegerField(null=True, blank=True)
    home_adress = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    certificates = models.FileField(upload_to='data/', null=True, blank=True)
    family_data = models.FileField(upload_to='data/', null=True, blank=True)
    profile_picture = models.FileField(upload_to='photos/', null=True, blank=True)
