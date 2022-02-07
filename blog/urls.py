from django.urls import path #importando função url
from . import views #importando todas as view do app blog, ainda ser criadas

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
