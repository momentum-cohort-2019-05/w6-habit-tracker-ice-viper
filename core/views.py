from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.db.models import Max, Q, Avg, Min
from core.forms import RecordForm, HabitForm
from django.contrib import messages
from datetime import date, timedelta


# Create your views here.
def welcome_page(request):

    return render(request, 'welcome_page.html', context={})


@login_required
def all_habits(request):
    habits_list = Habit.objects.filter(user=request.user).annotate(latest_record=Max(
        'dailyrecord__record_date', ))

    return render(request, "user_habits.html", {
        'habits_list': habits_list,
    })


@login_required
def record_create(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)
    record_date = request.POST.get('record_date', date.today())
    try:
        record = habit.dailyrecord_set.get(record_date=record_date)
    except DailyRecord.DoesNotExist:
        record = DailyRecord(habit=habit, record_date=record_date)

    if request.method == "POST":
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            messages.success(request, "Your record was created successfully.")
            return redirect('user_habits')
    else:
        form = RecordForm()

    return render(request, 'record_create.html', {
        "habit": habit,
        "form": form
    })


@login_required
def habit_create(request):

    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, "Your habit was created successfully.")
            return redirect('user_habits')
    else:
        form = HabitForm()

    return render(request, 'habit_create.html', {"form": form})


@login_required
def habit_detail(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)
    all_records = []
    for record in DailyRecord.objects.filter(
            habit=habit).order_by('-record_date'):
        all_records.append(record)
    # all_records.reverse()

    # habits_plus = Habit.objects.annotate(
    #     best_day=Max('dailyrecord__num_actions', filter=Q(name=habit.name)))
    habits_plus = Habit.objects.filter(name=habit.name).annotate(
        best_day=Max('dailyrecord__num_actions', ))
    habits_plus = habits_plus[0]

    oldest_record = Habit.objects.filter(name=habit.name).annotate(
        get_oldest=Min('dailyrecord__record_date', ))
    oldest_record = oldest_record[0].get_oldest

    habit_avg = Habit.objects.filter(name=habit.name).aggregate(
        avg_day=Avg('dailyrecord__num_actions', ))

    return render(request,
                  "habit_detail.html",
                  context={
                      'habits_plus': habits_plus,
                      'all_records': all_records,
                      'habit': habit,
                      'habit_avg': habit_avg,
                      'oldest_record': oldest_record
                  })
