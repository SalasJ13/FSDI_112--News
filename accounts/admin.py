from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role, Department


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'department', 'years')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'department', 'years')}),
    )
    list_display = [
        'username', 'email', 'role',
        'department', 'years', 'is_staff'
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Department)
