from rest_framework import serializers
from api.models import Answer
from api.serializer.alternatives_serializer import AlternativeSerializer, AlternativeGetSerializer


class AnswerGetSerializer(serializers.ModelSerializer):

    answered = AlternativeGetSerializer()

    class Meta:
        model = Answer
        fields = [
            'answered',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
