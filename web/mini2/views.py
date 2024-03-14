from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request, '1.html')

