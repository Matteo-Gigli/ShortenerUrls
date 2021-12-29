from django.db import models

#First of all we create the model to rappresent our url...
#We want to set short url with maximum 10 char.
#We have to declare the normal url as UrlField, we will need it later...
#Make migrations, make migrate.
#Now we go to admin.py to register our model.

class ShortingUrls(models.Model):
    shortUrl = models.CharField(max_length=10)
    normalUrl = models.URLField('URL', unique=True)