from rest_framework import serializers
from api.models import Exercise
from api.serializer.alternatives_serializer import AlternativeSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    alternatives = AlternativeSerializer(source='alternative_set', many=True)


    class Meta:
        model = Exercise
        fields = [
            'id',
            'order_num',
            'title',
            'description',
            'question',
            'alternatives'
        ]

