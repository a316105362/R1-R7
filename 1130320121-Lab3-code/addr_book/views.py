# -*- coding: utf-8 -*-
from django.http import HttpResponse
from addr_book.models import *
from django.template import Context
from django.shortcuts import render_to_response

def first(requset):
    return render_to_response("first.html")

def glance(request):
     book_list = Book.objects.all()  
     return render_to_response("addr_book.html", 
                               {"book_list":book_list})

def detail(request):
     i = request.GET["book_ISBN"]
     book = Book.objects.get(ISBN=i)
     author = book.AuthorID
     return render_to_response("detail.html",
          {'b': book, 'author': author})

def delete(request):
     i = request.GET["book_ISBN"] 
     p = Book.objects.filter(ISBN=i)
     p.delete()
     return render_to_response("delete.html")

     
def update(request):  
    i = request.GET["book_ISBN"]
    p = Book.objects.get(ISBN=i)
    c = Context({"p":p,})
    return render_to_response("update.html",c)

def update_author(request):  
    if request.POST:
        post = request.POST
        try:
            author = Author.objects.get(AuthorID = post["AuthorID"])
        except:
            
            return render_to_response('update_author.html')
        else:
            old_book = Book.objects.get(ISBN=request.GET["ISBN"])
            new_book = Book(
                ISBN = request.GET["ISBN"],
                Title = old_book.Title,
                AuthorID = author,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])          
            new_book.save()
            return render_to_response('insert_success2.html')
    else:
        return render_to_response('input_nothing1.html')



def new_author1(request):
    if request.POST:
        post = request.POST
        new_auhtor = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"])
        new_auhtor.save()
        return render_to_response('insert_success1.html')
    else:
        return render_to_response('input_nothing1.html')



def insert(request):
    return render_to_response("form.html")

def insert_author(request):
    if request.POST:
        post = request.POST
        try:
            author = Author.objects.get(AuthorID = post["AuthorID"])
        except:
            
            return render_to_response('insert_author.html')
        else:
            new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
                AuthorID = author,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])          
            new_book.save()
            return render_to_response('insert_success.html')
    else:
        return render_to_response('input_nothing.html')



def new_author(request):
    if request.POST:
        post = request.POST
        new_auhtor = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"])
        new_auhtor.save()
        return render_to_response('insert_success.html')
    else:
        return render_to_response('input_nothing.html')

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
   if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        author = Author.objects.filter(Name = q)
        book = []
        if (author != []):
            for a in author:
                book_list = a.book_set.all()
                if (book_list != []):
                    for b in book_list:
                        book.append(b)
        return render_to_response('search_results.html',
          {'book': book, 'author': author, 'query': q})
   else:
       return render_to_response('search_nothing.html')