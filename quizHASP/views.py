from django.shortcuts import render

def base(request):
    return render(request, 'base.html')


def about(request):
    name = 'messages about tests'
    return render(request, 'about.html', {'name': name})


