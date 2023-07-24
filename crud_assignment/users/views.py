from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# View for creating a new user (HTTP POST request)
class CreateUserView(generics.CreateAPIView):
    # Queryset to fetch all User objects from the database
    queryset = User.objects.all()
    
    # Serializer class used to serialize/deserialize User objects
    serializer_class = UserSerializer

# View for reading, updating, and deleting a user by username (HTTP GET, PUT, DELETE requests)
class ReadUpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    # Queryset to fetch all User objects from the database
    queryset = User.objects.all()
    
    # Serializer class used to serialize/deserialize User objects
    serializer_class = UserSerializer
    
    # The field used to look up the User object (in this case, 'username')
    lookup_field = 'username'