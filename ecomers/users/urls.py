from django.urls import path
from . import views

urlpatterns = [
    path('admin/users/', views.user_admin, name='user_admin'),
]