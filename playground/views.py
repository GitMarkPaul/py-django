from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lists():
    x = [1, 2, 3, 4, 5]
    return x

def say_hello(request):
    numbers = lists()
    
    return render(request, 'hello.html', {
        'numbers': numbers
    })