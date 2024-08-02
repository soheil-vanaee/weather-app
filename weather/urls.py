from django.contrib import admin
from django.urls import path
from weather import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('weather/', views.index, name='weather'),
    path('contact/', views.contact, name='contact'),
]
