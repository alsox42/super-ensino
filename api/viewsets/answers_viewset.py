from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Answer
from api.serializer import answers_serializer
from api.services import answers_service


class AnswerViewSet(ModelViewSet):
    queryset = answers_service.list_answers()
    serializer_class = answers_serializer.AnswerSerializer
    http_method_names = ['post']
