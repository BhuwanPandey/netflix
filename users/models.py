from django.db import models
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        default="profile/default.jpg",
        upload_to= "users/profile"
    )

    def __str__(self):
        return f'Profile of {self.user.username}'
    
    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.photo.path:
            img = Image.open(self.photo.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.photo.path)
