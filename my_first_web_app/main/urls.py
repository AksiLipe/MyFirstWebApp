from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"), #Делаем для главной страницы ссылку на views из другого приложения
    path('about/', views.about, name="about") #Делаем для 'О нас' ссылку на views из другого приложения
]