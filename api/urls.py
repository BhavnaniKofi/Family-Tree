from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamilyPicturesViewSet

router = DefaultRouter()
router.register(r'family-pictures', FamilyPicturesViewSet)

# Use the API endpoints at /api/family-pictures/ to interact with the data

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]