from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'), #главная
    path('about', views.about, name = 'about'), #about
]