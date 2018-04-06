from django.shortcuts import render

def IndexView():
    return render(request, 'index.html')
