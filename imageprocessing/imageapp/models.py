from django.db import models

# Create your models here.
class awsimage(models.Model):
    title=models.CharField(max_length=35)
    images=models.ImageField('images/')
