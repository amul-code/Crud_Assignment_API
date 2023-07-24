from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # We want to add a field for 'age' to the User model representation
    age = serializers.SerializerMethodField()

    class Meta:
        # Associate the serializer with the User model
        model = User
        # Define the fields that should be included in the serialized output
        fields = ('username', 'name', 'dob', 'gender', 'age')

    def get_age(self, obj):
        # Calculate the user's age based on the date of birth (dob)
        from datetime import date
        today = date.today()
        age = today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))
        return age
