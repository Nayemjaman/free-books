from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# core = booksite
def index(request):
    recommended_books = Book.objects.filter(recommended_books=True)
    fiction_books = Book.objects.filter(fiction_books=True)
    business_books = Book.objects.filter(business_books=True)
    context = {
        'recommended_books': recommended_books,
        'fiction_books': fiction_books,
        'business_books': business_books
    }
    return render(request, 'index.html', context)


def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'all_books.html', context)


def category_detail(request, slug):
    categories = Category.objects.get(slug=slug)
    context = {
        'categories': categories
    }
    return render(request, 'category_detail.html', context)


@login_required(login_url='user_login')
def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    books_category = book.category.first()
    similar_books = Book.objects.filter(
        category__name__startswith=books_category)
    context = {
        'book': book,
        'similar_books': similar_books,
        'books_category': books_category
    }
    return render(request, 'book_detail.html', context)


def search_book(request):
    search_books = Book.objects.filter(
        title__icontains=request.POST.get('name_of_book'))
    return render(request, 'search_book.html', {'search_books': search_books})


def register(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, "Account Created Successfully!")
            return redirect('user_login')

    context = {'register_form': register_form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid User")
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('index')
