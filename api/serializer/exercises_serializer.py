from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.models import Exercise
from api.serializer.alternatives_serializer import AlternativeSerializer
from api.serializer.answers_serializer import AnswerSerializer, AnswerGetSerializer
from api.serializer.exercise_group_serializer import ExerciseGroupSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    exercise_group = ExerciseGroupSerializer()
    alternatives = AlternativeSerializer(source='alternative_set', many=True)
    answer = AnswerGetSerializer(source='answer_set', many=True)

    class Meta:
        model = Exercise
        fields = [
            'id',
            'exercise_group',
            'order_num',
            'description',
            'alternatives',
            'answer'
        ]