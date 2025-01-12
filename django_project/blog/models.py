from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #onetomany, if user is deleted all post will be deleted

    def __str__(self):
        return self.title