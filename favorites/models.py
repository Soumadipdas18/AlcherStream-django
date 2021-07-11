from django.db import models

class Favorites(models.Model):
    movie_id=models.AutoField
    movie_name= models.CharField(max_length=50, default="")
    movie_desc= models.CharField(max_length=500, default="")
    image=  models.CharField(max_length=500, default="")
    userid= models.CharField(max_length=10,default="")
    def __str__(self):
        return self.movie_name