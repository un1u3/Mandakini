from django.db import models
from django.contrib.auth.models import User #place where django stores users

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE) #If the user is deleted the user is deleted 
    def __str__(self):
        return self.title
    