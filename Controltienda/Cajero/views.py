from django.shortcuts import render


def index(request):
    return render(request, 'Cajero/index.html')
