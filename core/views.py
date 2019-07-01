from django.shortcuts import render


# Create your views here.
def welcome_page(request):


    context = {

    }

    return render(request, 'welcome_page.html', context=context)