from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Organizer, Event, Schedule

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']
    list_filter = ['department']
    search_fields = ['user__username', 'department']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location', 'organizer']
    list_filter = ['date', 'organizer__department']
    search_fields = ['name', 'description']
    date_hierarchy = 'date'

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'start_time', 'end_time']
    list_filter = ['event__date', 'start_time']
    search_fields = ['title', 'description']
