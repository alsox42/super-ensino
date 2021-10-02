from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from api.models import Answer


class PerformanceSumaryAPIView(ViewSet):


    def list(self, request):
        tt_answers = Answer.objects.filter(user=request.user).count()
        tt_hits = Answer.objects.filter(user=request.user, answered__is_right=True).count()
        tt_mistakes = Answer.objects.filter(user=request.user, answered__is_right=False).count()
        enjoyment = 0

        try:
            enjoyment = ( tt_hits / tt_answers ) * 100
        except ZeroDivisionError:
            pass

        finally:
            return Response(
                {
                    'total de acertos': tt_hits,
                    'total de erros': tt_mistakes,
                    'aproveitamento': enjoyment
                })
