from django.urls import path #importando função url
from . import views #importando todas as views do app blog, ainda ser criadas

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
