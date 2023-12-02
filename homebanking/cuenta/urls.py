from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cuenta import views


router = DefaultRouter()
router.register(r'cuenta', views.CuentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]