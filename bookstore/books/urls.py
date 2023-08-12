from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('loghome/',views.loghome,name='loghome'),
    path('index/', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),

    # Add more URL patterns as needed for other views
]
