from main.admin import BasketAdmin
from django.contrib import admin
from user.models import User, EmailVerification




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',) 
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expirations',)
    fields = ('code', 'user', 'expirations', 'created',)
    readonly_fields = ('created',)