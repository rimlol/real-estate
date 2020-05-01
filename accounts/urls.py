from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name = 'login'), #главная листингов
    path('register', views.register, name = 'register'), #переход на страницу индвидуального листинга
    path('logout', views.logout, name = 'logout'), #поиск
    path('dashboard', views.dashboard, name = 'dashboard'), #поиск

]