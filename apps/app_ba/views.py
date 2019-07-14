from django.shortcuts import render, redirect, HttpResponse
from apps.app_ba.models import *

# Create your views here.
def index(request):
    all_books = Book.objects.all()

    context = {
        "all_books": all_books
    }

    return render(request, "app_ba/index.html", context)

def authors(request):
    all_authors = Author.objects.all()

    context = {
        "all_authors": all_authors
    }

    return render(request, "app_ba/authors.html", context)


def add_book(request):
    new_book = Book.objects.create(**copy_dict_partial(request.POST.dict()))
    print(new_book)
    return redirect("/")

def copy_dict_partial(source_dict, keys_to_remove=[]):
    copy = source_dict.copy()
    if "csrfmiddlewaretoken" in copy: 
        keys_to_remove.append("csrfmiddlewaretoken")
    
    for key in keys_to_remove:
        del copy[key]
    
    return copy

def add_author(request):
    new_author = Author.objects.create(first_name = request.POST["first_name"], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect("/authors")

def display_author(request, author_id):
    all_books = Book.objects.all()
    author = Author.objects.get(id = author_id)
    context = {
        "author": author,
        "authors_books": author.books.all(),
        "all_books": all_books,
    }
    return render(request, "app_ba/display_author.html", context)

def append_book(request, author_id):
    auth = Author.objects.get(id = author_id)
    bk = Book.objects.get(id = request.POST['book_titles'])
    bk.authors.add(auth)

    all_books = Book.objects.all()
    author = Author.objects.get(id = author_id)
    context = {
        "author": author,
        "authors_books": author.books.all(),
        "all_books": all_books,
    }
    return render(request, "app_ba/display_author.html", context)