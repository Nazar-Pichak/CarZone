from django.db import models


# Create your models here.

class Team(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=225)
    twitter_link = models.URLField(max_length=225)
    google_plus_link = models.URLField(max_length=225)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name}'
    
    
    