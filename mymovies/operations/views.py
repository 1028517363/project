from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')


def movies(request):
    return render(request, 'movies.html')


def single(request):
    return render(request, 'single.html')


def shows(request):
    return render(request, 'shows.html')


def sports(request):
    return render(request, 'sports.html')


def history(request):
    return render(request, 'history.html')