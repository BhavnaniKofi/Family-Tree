from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from family_pictures.models import FamilyPictures
from .serializers import FamilyPicturesSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class FamilyPicturesViewSet(viewsets.ModelViewSet):
    queryset = FamilyPictures.objects.all()
    serializer_class = FamilyPicturesSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        """
        Optionally restricts the returned pictures by filtering
        against query parameters in the URL.
        """
        queryset = FamilyPictures.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name_of_family_member__icontains=name)
        return queryset
    
    @action(detail=True, methods=['get'])
    def image_url(self, request, pk=None):
        """
        Additional endpoint to get just the image URL if needed separately.
        """
        picture = self.get_object()
        url = picture.get_picture_url()
        return Response({'image_url': url})