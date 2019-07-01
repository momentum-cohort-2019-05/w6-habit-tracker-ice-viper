from django.contrib import admin

# Register your models here.
class HabitAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("user", "name")}

