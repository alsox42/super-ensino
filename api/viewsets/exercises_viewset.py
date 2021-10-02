from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Exercise
from api.serializer import exercises_serializer
from api.services import exercises_service


class ExerciseViewSet(ModelViewSet):

    queryset = exercises_service.list_exercises()
    serializer_class = exercises_serializer.ExerciseSerializer
    http_method_names = ['get']


    def get_queryset(self):
        order_num = self.request.query_params.get('ordernum', None)
        queryset = Exercise.objects.all()

        if order_num:
            queryset = queryset.filter(order_num=order_num)

        return queryset
