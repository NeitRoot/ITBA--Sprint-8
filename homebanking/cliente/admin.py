from django.contrib import admin

# Register your models here.
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('id')


admin.site.register(Cliente)
