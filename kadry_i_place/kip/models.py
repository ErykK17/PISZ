from django.db import models
from django.contrib.auth import get_user_model

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=10,
        choices=[
            ('kierownik', 'Kierownik'),
            ('pracownik', 'Pracownik')
            ] 
        )

