from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q


# Create your views here.
def welcome_page(request):

    return render(request, 'welcome_page.html', context={})


@login_required
def all_habits(request):
    habits_list = Habit.objects.annotate(latest_record=Max(
        'dailyrecord__created_on', filter=Q(user=request.user)))

    return render(request, "user_habits.html", {
        'habits_list': habits_list,
    })
