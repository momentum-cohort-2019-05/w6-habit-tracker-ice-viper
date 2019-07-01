from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from django.utils import timezone


# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=100)
    habit_goal = models.PositiveIntegerField(default=0)
    #True habit_types are positive habits
    habit_type = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(name, max_length=100, unique=True, null=True)
    # date_started = models.DateField(auto_now_add=True)
    units = models.CharField(max_length=30,)
    
    # def get_most_recent_record(self):
    #     most_recent_record = self.DailyRecord.get(pk=1)

    # def __str__(self):
    #     return self.name


class DailyRecord(models.Model):
    num_actions = models.PositiveIntegerField(default=0)
    # created_on = models.DateTimeField(default=timezone.now)
    created_on = models.DateField(default=date.today)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.created_on}, {self.habit}'