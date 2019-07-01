from django.contrib import admin
from core.models import Habit, Daily_Record

# Register your models here.
admin.site.register(Habit)
admin.site.register(Daily_Record)

# class HabitAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}



