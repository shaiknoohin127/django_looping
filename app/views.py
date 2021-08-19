from django.shortcuts import render

# Create your views here.
def for_looping(request):
    d={'place':'ARAKU'}
    return render(request,'looping.html',d)