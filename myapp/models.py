from django.db import models
import os

def memorial_image_profile_upload_path(instance, filename):
    """Path for profile memorial image"""
    memorial_name = instance.name.replace(' ', '_')
    return f'memorials/{memorial_name}_{instance.id}/images/{filename}'

def memorial_image_collection_upload_path(instance, filename):
    """Path for images in the collection"""
    memorial_name = instance.memorial.name.replace(' ', '_')
    return f'memorials/{memorial_name}_{instance.memorial.id}/image_collection/{filename}'

class Memorial(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to=memorial_image_profile_upload_path, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # If this is a new instance, save first to get an ID
        if not self.id:
            super().save(*args, **kwargs)
        
        # Now save again to use the ID in the file path
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} #{self.id}"
    
class MemorialImage(models.Model):
    memorial = models.ForeignKey(Memorial, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=memorial_image_collection_upload_path)
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']    