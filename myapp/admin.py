from django.contrib import admin
from .models import Memorial, MemorialImage

class MemorialImageInline(admin.TabularInline):
    model = MemorialImage
    extra = 1

@admin.register(Memorial)
class MemorialAdmin(admin.ModelAdmin):
    inlines = [MemorialImageInline]
    list_display = ['name', 'id']

@admin.register(MemorialImage)
class MemorialImageAdmin(admin.ModelAdmin):
    list_display = ['memorial', 'order', 'caption']
    list_filter = ['memorial']