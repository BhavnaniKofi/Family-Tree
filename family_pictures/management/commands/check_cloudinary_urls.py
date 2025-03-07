from django.core.management.base import BaseCommand
from family_pictures.models import FamilyPictures

class Command(BaseCommand):
    help = 'Check all Cloudinary URLs to ensure they use HTTPS'

    def handle(self, *args, **options):
        all_pictures = FamilyPictures.objects.all()
        for picture in all_pictures:
            url = picture.get_picture_url()
            if url:
                if url.startswith('https://'):
                    self.stdout.write(self.style.SUCCESS(
                        f'✓ {picture.name_of_picture}: URL uses HTTPS: {url}'
                    ))
                else:
                    self.stdout.write(self.style.ERROR(
                        f'✗ {picture.name_of_picture}: URL does NOT use HTTPS: {url}'
                    ))
            else:
                self.stdout.write(self.style.WARNING(
                    f'! {picture.name_of_picture}: No URL available'
                ))