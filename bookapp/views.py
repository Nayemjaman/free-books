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

def all_books(request):
    books =Book.objects.all()
    context = {
        'books': books
    }
    return render(request,'all_books.html', context)


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    context ={
        'category': category
    }
    return render(request, 'category_detail.html', context)

def book_detail(request,slug):
    book = Book.objects.get(slug=slug)
    books_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith=books_category)
    context = {
        'book': book,
        'similar_books': similar_books,
        'books_category':books_category
    }
    return render(request, 'book_detail.html',context)


def search_book(request):
    search_books =  Book.objects.filter(title__icontains=request.POST.get('name_of_book'))
    return render(request,'search_book.html',{'search_books':search_books})