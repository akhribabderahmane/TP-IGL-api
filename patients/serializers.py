from rest_framework import serializers
from .models import Patient, Dpi
from users.models import User, Medcin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'telephone', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class DpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dpi
        fields = ['id', 'created_at', 'antecedants', 'bilan_biologique']
        read_only_fields = ['created_at']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    dpi = DpiSerializer(read_only=True)
    
    class Meta:
        model = Patient
        fields = ['id', 'user', 'nss', 'date_naissance', 'addresse', 'mutuelle', 
                 'medcin_traitant', 'personne_contact', 'dpi']
        read_only_fields = ['dpi']

    def create(self, validated_data):
        # Extract user data from validated_data
        user_data = validated_data.pop('user')
        # Add role to user_data
        user_data['role'] = 'patient'
        
        # Create user
        user = User.objects.create(**user_data)
        
        # Create empty DPI
        dpi = Dpi.objects.create()
        
        # Create patient with the user and DPI
        patient = Patient.objects.create(
            user=user,
            dpi=dpi,
            **validated_data
        )
        
        return patient

    def update(self, instance, validated_data):
        # Handle nested user update
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            user = instance.user
            
            # Update user fields
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()
        
        # Update patient fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance
    
class DpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dpi
        fields = '__all__'