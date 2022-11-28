from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('all_books', views.all_books, name='all_books'),
    path('category_detail/<str:slug>',
         views.category_detail, name='category_detail'),
    path('book_detail/<str:slug>', views.book_detail, name='book_detail'),
    path('search_book', views.search_book, name='search_book'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),

]
