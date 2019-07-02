from django import forms
from core.models import Habit, DailyRecord

class RecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = (
            'record_date',
            'num_actions',
        )

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = (
            'name',
            'habit_goal',
            'habit_type',
            'units',
        )