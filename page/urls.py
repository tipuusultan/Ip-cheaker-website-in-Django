from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path('', views.home , name="home"),
    path('web-scrapping' , views.scrapping ,  name="webscrapping"),
    path('result/' , views.result , name="Final")

]
