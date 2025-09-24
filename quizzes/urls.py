from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizzViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizzViewSet)

urlpatterns = [
    path('admin/', include('django.contrib.admin.urls')),
    path('api/', include(router.urls)),
    ]