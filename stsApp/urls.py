
from django.urls import path

from . import views
from .views import AboutPageView
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', HomePageView.as_view(), name='About us'),
    path('login/', views.login, name="login"),
    path('Checkplag/', views.Checkplag, name="Checkplag"),
    path('register/', views.register, name="register"),
    path('results/', views.results, name="results"),
    path('dictionary/', views.dictionary, name="dictionary"),
    path('student/', views.student, name='student'),
    path('home/', views.plag_home, name='Plag_Home'),
]