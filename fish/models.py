from django.db import models

# Create your models here.


class Fish(models.Model):
	name = models.CharField(max_length=50)
	species = models.CharField(max_length=50)
	weight = models.IntegerField()
	length = models.IntegerField()
	latitude = models.CharField(max_length=30)
	longitude = models.CharField(max_length=30)
	image = models.ImageField(upload_to='fish' ,null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

