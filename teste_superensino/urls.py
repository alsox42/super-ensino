from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from api.viewsets import (
     exercises_viewset, answers_viewset, performance_sumary_viewset
)


router = routers.DefaultRouter()

router.register('exercicios', exercises_viewset.ExerciseViewSet)
router.register('respostas', answers_viewset.AnswerViewSet)
router.register("resumo-de-desempenho", performance_sumary_viewset.PerformanceSumaryAPIView, basename='teste')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token)


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
