from django.contrib import admin
from core.models import Habit, DailyRecord

# Register your models here.
admin.site.register(Habit)
admin.site.register(DailyRecord)

# class HabitAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}



