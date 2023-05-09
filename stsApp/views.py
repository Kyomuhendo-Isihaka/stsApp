from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    # context_object_name = {'title': 'Home'}


class AboutPageView(TemplateView):
    template_name = 'about.html'
    # context_object_name = {'title': 'About us'}


def login(request):
    context = {" title": "Login"}
    return render(request, 'login.html', context)


def register(request):
    return render(request, 'register.html')


def Checkplag(request):
    return render(request, "Checkplag.html")


def dictionary(request):
    return render(request, 'dictionary.html')


def results(request):
    return render(request, 'results.html')


def student(request):
    return render(request, 'student.html')


def plag_home(request):
    return render(request, 'plag_home.html')
