from django.contrib import admin

from .models import UnidadeDeMedida, Papelao, Papel, Plastico, Usuario

# Register your models here.
admin.site.register(UnidadeDeMedida)
admin.site.register(Papelao)
admin.site.register(Papel)
admin.site.register(Plastico)
admin.site.register(Usuario)