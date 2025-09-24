from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizzViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizzViewSet)

urlpatterns = [
    path('', include(router.urls)),  # rutas del API
]
