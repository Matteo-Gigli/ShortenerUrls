from django.contrib import admin
from .models import ShortingUrls

#Importing the models and create a superuser.
#Now we can start to build our views...
#First we have to declare a shorting.py and a forms.py
#Go to shorting.py

admin.site.register([ShortingUrls])
