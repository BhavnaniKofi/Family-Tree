from django.contrib import admin
from django.utils.html import format_html
from .models import FamilyPictures

@admin.register(FamilyPictures)
class FamilyPicturesAdmin(admin.ModelAdmin):
    list_display = ('name_of_family_member', 'date_of_birth', 'name_of_picture', 'image_preview', 'created_at')
    list_filter = ('name_of_family_member', 'date_of_birth')
    search_fields = ('name_of_family_member', 'name_of_picture', 'description_of_picture')
    readonly_fields = ('created_at', 'updated_at', 'image_preview', 'image_url')
    fieldsets = (
        ('Family Member Information', {
            'fields': ('name_of_family_member', 'date_of_birth')
        }),
        ('Picture Information', {
            'fields': ('name_of_picture', 'description_of_picture', 'picture', 'image_preview', 'image_url')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        """Display a thumbnail of the image in the admin list view"""
        if obj.picture:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.get_picture_url())
        return "-"
    image_preview.short_description = 'Image Preview'
    
    def image_url(self, obj):
        """Display the full HTTPS URL in the admin detail view"""
        if obj.picture:
            return format_html('<a href="{0}" target="_blank">{0}</a>', obj.get_picture_url())
        return "-"
    image_url.short_description = 'Full Image URL (HTTPS)'