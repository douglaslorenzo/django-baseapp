from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'tasks.html')

def inserir(request):
    nome = "douglas"
    return render(request,'templates.html', {'nome':'douglas'})