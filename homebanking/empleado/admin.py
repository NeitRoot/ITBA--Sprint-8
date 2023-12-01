from django.contrib import admin

# Register your models here.
from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ('id')


admin.site.register(Empleado)
