from django.contrib import admin
from mapApp.models import *
# Register your models here.


admin.site.site_header = 'Map Admin'
admin.site.register(search)