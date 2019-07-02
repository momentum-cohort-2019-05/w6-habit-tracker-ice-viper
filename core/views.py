from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.db.models import Max, Q, Avg
from core.forms import RecordForm
from django.contrib import messages


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
def record_create(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)

    if request.method == "POST":
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            messages.success(request, "Your card was created successfully.")
            return redirect('user_habits')
    else:
        form = RecordForm()

    return render(request, 'record_create.html', {
        "habit": habit,
        "form": form
    })

@login_required
def habit_detail(request):
    habits_plus = Habit.objects.annotate(
        best_day=Max('dailyrecord__num_actions'),
        avg_day=Avg('dailyrecord__num_actions'))

    return render(request,
                  "habit_detail.html",
                  context={'habits_plus': habits_plus})

