

# Register your models here.
from django.contrib import admin

from .models import Vhigh,High,Med

admin.site.register(Vhigh)

admin.site.register(High)
admin.site.register(Med)