from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Imagine all the people living life in peace'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("""<h1>Rango says here is the About page.</h1>
                        <p><a href="/rango/">Index</a></p>""")