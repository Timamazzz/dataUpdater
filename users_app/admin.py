from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Organization


# Register your models here.
class UserInline(admin.StackedInline):
    model = User.organizations.through
    extra = 1


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('email',)
    inlines = [UserInline]


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created', 'updated')
    search_fields = ('name', 'inn', 'kpp', 'ogrn', 'okved')
    list_filter = ('is_active',)
    ordering = ('created',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Organization, OrganizationAdmin)
