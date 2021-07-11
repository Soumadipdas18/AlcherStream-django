from django.db import models

class BlockBuster(models.Model):
    movie_id=models.AutoField
    movie_name= models.CharField(max_length=50, default="")
    movie_desc= models.CharField(max_length=500, default="")
    image=  models.CharField(max_length=500, default="")
    def __str__(self):
        return self.movie_name