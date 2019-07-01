from django.contrib import admin
from core.models import Habit, Record

# Register your models here.
admin.site.register(Habit)
admin.site.register(Record)

# class HabitAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}



