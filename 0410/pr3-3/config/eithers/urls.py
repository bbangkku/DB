
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/comment',views.comment,name='comment'),
    path('random/',views.random, name='random'),

]
