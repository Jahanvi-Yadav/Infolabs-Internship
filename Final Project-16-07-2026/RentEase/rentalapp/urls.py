from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.properties, name='properties'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('booking/<int:id>/', views.booking, name='booking'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('payment/<int:id>/', views.payment, name='payment'),
    path('review/<int:id>/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout_view, name='logout'),
]