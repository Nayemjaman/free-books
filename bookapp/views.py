from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
# core = booksite
def index(request):
    recommended_books = Book.objects.filter(recommended_books= True)
    fiction_books = Book.objects.filter(fiction_books= True)
    business_books = Book.objects.filter(business_books= True)
    context = {
        'recommended_books':recommended_books,
        'fiction_books':fiction_books,
        'business_books':business_books
    }
    return render(request, 'index.html', context)
