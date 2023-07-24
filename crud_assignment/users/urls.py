from django.urls import path
from .views import CreateUserView, ReadUpdateDeleteUserView
urlpatterns = [
     path('users/', CreateUserView.as_view(), name='create-user'),  # Use CreateUserView for creating users (POST)
    path('users/<str:username>/', ReadUpdateDeleteUserView.as_view(), name='user-details'),
]
