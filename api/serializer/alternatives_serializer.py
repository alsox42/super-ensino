from rest_framework import serializers
from api.models import Alternative

class AlternativeGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternative
        fields = [
            'letter',
            'text',
        ]

class AlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternative
        fields = '__all__'
