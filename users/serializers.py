from rest_framework import serializers
from .models import User, UserRole

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=UserRole.choices)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        # Check if user exists with the provided email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        # Check if the password matches
        if user.password != password:  # Assuming plain-text passwords; consider hashing!
            raise serializers.ValidationError("Invalid email or password.")

        # Check if the role matches
        if user.role != role:
            raise serializers.ValidationError("Role mismatch for the provided email.")

        # Return validated user
        data["user"] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "nom", "prenom", "telephone", "email", "role"]
