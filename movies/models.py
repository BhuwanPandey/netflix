from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Resize
from multiselectfield import MultiSelectField

genre = (
    ("adventure","Adventure"),
    ("comedy","Comedy"),
    ("crime","Crime"),
    ("fantasy","Fantasy"),
    ("historical","Historical"),
    ("horror","Horror"),
    ("romance","Romance"),
    ("sci-fi","Sci-fi"),
    ("thriller","Thriller"),
    ("western","Western"),
    ("animation","Animation"),
    ("drama","Drama"),
    ("documentary","Documentary")
)
class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="movies/images")
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Resize(500, 250)],
        options={'quality': 100}
    )
    trailer = models.FileField(upload_to="movies/trailer",blank=True, null=True)
    published_date = models.DateField(null=True,blank=True)
    imdb_rating = models.FloatField(default=0)
    genre = MultiSelectField(choices=genre)
    isseries = models.BooleanField(blank=False)

    def __str__(self) -> str:
        return f"{self.title}"

class MovieList(models.Model):
    title = models.CharField(max_length=100,unique=True)
    type = models.CharField(choices=[("movies","Movies"),("series","Series")],max_length=15)
    content = models.ManyToManyField(Movies)
    
    def __str__(self) -> str:
        return f"{self.title}"
