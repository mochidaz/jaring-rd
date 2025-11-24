from django.shortcuts import render

from .models import Circle


def about_view(request):
    return render(request, 'about/about.html')


def circle_list(request):
    circles = Circle.objects.all()
    return render(request, 'about/circle_list.html', {'circles': circles})
