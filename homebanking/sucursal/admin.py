from django.contrib import admin

# Register your models here.
from .models import Sucursal


class SucursalAdmin(admin.ModelAdmin):
    readonly_fields = ('id')


admin.site.register(Sucursal)
