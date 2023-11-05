from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.post.title
