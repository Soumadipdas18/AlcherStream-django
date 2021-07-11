from django.db import models
import uuid
class Reviews(models.Model):
    movie_id=models.AutoField
    movie_name= models.CharField(max_length=50, default="")
    movie_desc= models.CharField(max_length=500, default="")
    image=  models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.movie_name


class Comments(models.Model):
    movie_id=models.AutoField
    comment_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    image=  models.CharField(max_length=500, default="")
    who_commented=models.CharField(max_length=10, default="")
    what_commented=models.CharField(max_length=1000, default="")
    when_commented=models.DateTimeField()
    def __str__(self):
        return self.image