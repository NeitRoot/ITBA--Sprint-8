from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet


router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]

#http://127.0.0.1:8000/cliente/cliente/1/
