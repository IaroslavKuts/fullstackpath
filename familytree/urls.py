from django.urls import path
from . import views



urlpatterns = [
    path('', views.Index_Page.as_view(), name='index'),
    path('UserPage/', views.User_Page.as_view(), name='UserPage'),
    path('registration/', views.Registration_Page.as_view(), name='registrate'),
]
