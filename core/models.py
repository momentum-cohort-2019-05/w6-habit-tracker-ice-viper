from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.name


class Daily_Record(models.Model):
    num_actions = models.PositiveIntegerField(default=0)
    created_on = models.DateField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.created_on}, {self.habit}'