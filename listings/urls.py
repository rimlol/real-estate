from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'listings'), #главная листингов
    path('<int:listing_id>', views.listing, name = 'listing'), #переход на страницу индвидуального листинга
    path('search', views.search, name = 'search'), #поиск
]