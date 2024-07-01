from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to= "users/profile",
        blank=True
    )

    def __str__(self):
        return f'Profile of {self.user.username}'

