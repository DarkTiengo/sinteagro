from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User

u = UserAdmin

u.fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name','sexo','nascimento','estado','cidade')}),
        (('Permissions'), {'fields': ('is_trusty', 'is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

u.add_fieldsets = ((None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

u.ordering = ('email',)
u.list_display = ('email', 'first_name', 'last_name', 'is_staff')

admin.site.register(User, u)


