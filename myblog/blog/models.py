from django.db import models

# Create your models here.
class Post(models.Model):
    heading = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField()
    author = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

