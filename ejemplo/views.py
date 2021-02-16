from django.shortcuts import render
from bdb import foo

# Create your views here.

def noticia_list(request):
    
    return render(request, 'ejemplo/noticia_list.html', {})
