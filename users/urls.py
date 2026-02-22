from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
]