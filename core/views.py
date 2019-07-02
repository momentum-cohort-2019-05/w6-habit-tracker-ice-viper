from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required

from django.db.models import Max, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
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




class DailyRecordCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = DailyRecord
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})

@login_required
def habit_detail(request):
    habits_plus = Habit.objects.annotate(
        best_day=Max('dailyrecord__num_actions'),
        avg_day=Avg('dailyrecord__num_actions'))

    return render(request,
                  "habit_detail.html",
                  context={'habits_plus': habits_plus})

