from django.shortcuts import render
from django.http import HttpResponse

def funcao_login(request):
    return render(request, 'tela_login.html')

