from rest_framework import serializers
from api.models import ExerciseGroup


class ExerciseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseGroup
        fields = [
            'text',
            'the_amount'
        ]
