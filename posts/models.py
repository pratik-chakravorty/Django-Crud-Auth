from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    travel_headline = models.CharField(max_length=300)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    travel_itenary = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.travel_headline
