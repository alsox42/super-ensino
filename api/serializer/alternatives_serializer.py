from rest_framework import serializers
from api.models import Alternative


class AlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternative
        fields = [
            'id',
            'letter',
            'text',
            'is_right'
        ]
