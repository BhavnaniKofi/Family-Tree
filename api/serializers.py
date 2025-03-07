from rest_framework import serializers
from family_pictures.models import FamilyPictures

class FamilyPicturesSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()
    
    class Meta:
        model = FamilyPictures
        fields = ('id', 'name_of_family_member', 'date_of_birth', 'name_of_picture', 
                  'description_of_picture', 'picture', 'picture_url', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'picture_url')
    
    def get_picture_url(self, obj):
        """
        Get the full HTTPS URL for the Cloudinary image.
        This ensures frontend applications can access the image directly.
        """
        if obj.picture:
            # Force HTTPS instead of using whatever protocol is in the original URL
            url = obj.picture.url
            if url.startswith('http:'):
                url = url.replace('http:', 'https:', 1)
            return url
        return None