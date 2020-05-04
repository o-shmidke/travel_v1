from django.contrib import admin
from .models import *


class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route

    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ['travel_time']


admin.site.register(Route, RouteAdmin)
