from django.shortcuts import render, HttpResponse

# Create your views here.
# core = booksite
def index(request):
    return render(request, 'index.html')