from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'Index.html')

def ingresar(request):
    return render(request, 'login.html')

def gestion(request):
    return render(request, 'data.html')