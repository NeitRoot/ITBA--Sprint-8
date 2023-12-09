from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet

router = DefaultRouter()
router.register(r'empleado', EmpleadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#http://127.0.0.1:8000/empleado/empleado/1/




