from django.shortcuts import render
from django.http import HttpResponse

# http request
def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Ryan Shoiti',
    })