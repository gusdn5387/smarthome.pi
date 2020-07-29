from django.contrib import admin
from .models import LedStatus, RoomStatus

class LedStatusAdmin(admin.ModelAdmin):
    list_display = ('is_on', 'created_at')

class RoomStatusAdmin(admin.ModelAdmin):
    list_display = ('people_count', 'created_at')


admin.site.register(LedStatus, LedStatusAdmin)
admin.site.register(RoomStatus, RoomStatusAdmin)
