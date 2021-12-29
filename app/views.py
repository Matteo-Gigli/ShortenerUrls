from django.shortcuts import render,redirect
from .shorting import Sizing
from .models import ShortingUrls
from .forms import UrlsForm

# Now we can start with views.
# The first view we made is make.
# We want to refer about our form and we adding a string variable called a.
# We need of this to refer to the urls
# As we can see we imported the shorting.py to use the Sizing class created before.
# Now the magic happing, in fact we refers to the a variable as a Sizing().issue_token().
# This command allowed us to take the url and modifing the letters by Ascii, like we declered before.
# Then we save the new urls.
# We specifing even if there is no urls or non defined urls we have back 'Invalid Urls'.
# As you can see at the end we can close our function, passing by the context form, a.
# In this case we are talking about GET method and not POST method.

# Now we can setup home.
# This function have 2 parameters, request and token.
# First of all we are going to filter our queryset and we go to attach the shortUrl to the token.
# Then we call redirect functions to be redirected by the shortUrl, to the full url.
# It's something like an identification.

# Just the last things to do, like adding urls, to our cutter/urls.py.
# So go there.

def home(request, token):
    normalUrl = ShortingUrls.objects.filter(shortUrl=token)[0]
    return redirect(normalUrl.normalUrl)


def make(request):
    form = UrlsForm(request.POST)
    a = ''
    if request.method == 'POST':
        if form.is_valid():
            newUrls = form.save(commit=False)
            a = Sizing().issue_token()
            newUrls.shortUrl = a
            newUrls.save()
        else:
            form = UrlsForm()
            a = 'Invalid Urls'

    return render(request, 'home.html', context={'form': form, 'a': a})



