from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.viewsets import (
    exercises_viewset, answers_viewset
)
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register('exercicios', exercises_viewset.ExerciseViewSet)
router.register('respostas', answers_viewset.AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
