from django.urls import path

from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home), # Home

]