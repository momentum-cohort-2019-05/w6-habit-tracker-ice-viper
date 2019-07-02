from django import forms
from core.models import Habit, DailyRecord

class RecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = (
            'record_date',
            'num_actions',
        )