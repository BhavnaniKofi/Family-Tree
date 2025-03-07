from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
import cloudinary

class FamilyPictures(models.Model):
    name_of_family_member = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    name_of_picture = models.CharField(max_length=255)
    description_of_picture = models.TextField()
    picture = CloudinaryField('image')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Family Picture'
        verbose_name_plural = 'Family Pictures'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name_of_family_member} - {self.name_of_picture}"
    
    def get_picture_url(self):
        """Return the complete HTTPS URL for the Cloudinary image"""
        return self.picture.url if self.picture else None