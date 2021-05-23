from django.shortcuts import render
from datetime import datetime

# Create your views here.

def homepage(request):

    today = datetime.now()
    return render(request, 'homepage.html', 
        {'now':today, 'myname':'Toby', 'letters':list('abcdefg')})

def about(request, myname):
    return render(request, 'about.html', {'name':myname})