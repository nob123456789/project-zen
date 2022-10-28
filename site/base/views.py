from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def code(request):
    return render(request, 'code.html')

def documentation(request):
    return render(request, 'docs/button.html')

def e404(request):
    return render(request, '404.html')