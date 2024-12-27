from rest_framework import serializers
from .models import Examen, CompteRendu

class CompteRenduSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteRendu
        fields = "__all__"

class ExamenSerializer(serializers.ModelSerializer):
    compte_rendu = CompteRenduSerializer(required=False)  # Allow creating an Examen without a CompteRendu

    class Meta:
        model = Examen
        fields = "__all__"

    def create(self, validated_data):
        compte_rendu_data = validated_data.pop('compte_rendu', None)
        examen = Examen.objects.create(**validated_data)

        if compte_rendu_data:
            compte_rendu = CompteRendu.objects.create(**compte_rendu_data)
            examen.compte_rendu = compte_rendu
            examen.save()

        return examen
