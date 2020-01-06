from django.urls import path
from app_Folder import views


urlpatterns = [
    path("", views.home, name="home"),
    path('checkout/', views.checkout, name = 'checkout'),
]