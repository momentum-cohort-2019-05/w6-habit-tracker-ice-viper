"""habittracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from core import views
from django.conf.urls.static import static


urlpatterns = [
    path('', RedirectView.as_view(url='/welcome_page/')),
    path('welcome_page/', views.welcome_page, name='welcome_page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('user_habits', views.all_habits, name="user_habits"),
    path('record_create/<int:habit_pk>/', views.record_create, name='record_create'),
    path('habit_create/', views.habit_create, name='habit_create'),
    path('habit_detail/<int:habit_pk>/', views.habit_detail, name='habit_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
