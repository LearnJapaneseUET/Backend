from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('translateVtoJ/', views.translateVtoJ, name='translateVtoJ'),
    path('translateJtoV/', views.translateJtoV, name='translateJtoV'),
]
