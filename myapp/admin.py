from django.contrib import admin
from .models import Memorial, MemorialImage
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

# Unfold configuration
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import AutocompleteSelectFilter


class MemorialImageInline(TabularInline):
    model = MemorialImage
    extra = 1

@admin.register(Memorial)
class MemorialAdmin(ModelAdmin):
    inlines = [MemorialImageInline]
    list_display = ['name', 'id']
    list_filter = ['name', 'id']
    search_fields = ['name','id']

@admin.register(MemorialImage)
class MemorialImageAdmin(ModelAdmin):
    list_display = ['memorial', 'order', 'caption']
    list_filter = ['memorial']



# Unfold user and group config below
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
