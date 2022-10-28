from django.shortcuts import render

# Create your views here.
def locator(request, name):
    url = str('docs/'+name+'.html')
    return render(request, url)