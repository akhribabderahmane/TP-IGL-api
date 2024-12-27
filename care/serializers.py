from rest_framework import serializers
from .models import Soin


class SoinSerializer(serializers.ModelSerializer):
    """
    Serializer for Soin model.
    """

    class Meta:
        model = Soin
        fields = '__all__'
