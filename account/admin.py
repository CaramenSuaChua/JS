from django.contrib import admin
from .models import Account
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display =('name', 'email', 'is_staff')
admin.site.register(Account, AccountAdmin)