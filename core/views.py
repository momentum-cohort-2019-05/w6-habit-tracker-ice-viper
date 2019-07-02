from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q, Avg


# Create your views here.
def welcome_page(request):

    return render(request, 'welcome_page.html', context={})


@login_required
def all_habits(request):
    habits_list = Habit.objects.annotate(latest_record=Max(
        'dailyrecord__record_date', filter=Q(user=request.user)))

    return render(request, "user_habits.html", {
        'habits_list': habits_list,
    })


@login_required
def habit_detail(request):
    habits_plus = Habit.objects.annotate(
        best_day=Max('dailyrecord__num_actions'),
        avg_day=Avg('dailyrecord__num_actions'))

    return render(request,
                  "habit_detail.html",
                  context={'habits_plus': habits_plus})
