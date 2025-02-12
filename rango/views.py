from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Apple, Banana, Coconut and Dragonfruit'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'aboutmessage': 'This tutorial has been put together by Yuhe Lu.'}
    return render(request, 'rango/about.html', context=context_dict)