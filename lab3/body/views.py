# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,RequestContext,HttpResponseRedirect,Http404
from django.contrib.auth.forms import UserCreationForm
from django import forms
from body.models import Book,Author
#test for the use of github
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    },context_instance=RequestContext(request))

def search(request):
    if request.user.is_authenticated():
        errors = []
        if 'q' in request.GET:
            try:
                q = request.GET['q']
                if not q:
                    errors.append('请输入查询作者名') 
                else:
                    books = []
                    author = Author.objects.filter(Name=q) 
                    for a in author:
                        if a.book_set.all():
                            books.extend(a.book_set.all())
                    return render_to_response('search_results.html',
                        {'books': books, 'query': q})
            except:
                errors.append("图书馆未收录该作者！请检查作者名是否拼写正确")
        return render_to_response('search_form.html',{'errors': errors})
    else:
         return HttpResponseRedirect('/accounts/login/')
    
def book_detail(request,q):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(ISBN = q)
            author = book.AuthorID
        except ValueError:
            raise Http404()
        return render_to_response('detail.html',{'book':book, 'author':author})
    else:
        return HttpResponseRedirect('/accounts/login/')
    
def book_delete(request,q):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(ISBN = q)
            author = book.AuthorID
            q = author.Name
            book.delete()
        except ValueError:
            raise Http404()
        books = author.book_set.all()
        return render_to_response('search_results.html',
                        {'books': books, 'query': q})
    else:
        return HttpResponseRedirect('/accounts/login/')
  
def book_new(request):
    if request.user.is_authenticated():
        if request.POST:
            post = request.POST
            if post["ISBN"] and post["Title"] and post["AuthorID"] and post["Publisher"] and post['PublishDate'] and post['Price']:
                bo = Book.objects.all()
                isbn = []
                for b in bo:
                    isbn.append(b.ISBN)
                isb = post.get('ISBN', '')
                if (isb not in isbn):
                    t = post.get('Title', '')
                    au = post.get('AuthorID', '')
                    pler = post.get('Publisher', '')
                    plda = post.get('PublishDate', '')
                    prc = post.get('Price', '')
                    auth = Author.objects.get(id=int(au))
                    Book.objects.create(ISBN=isb, Title=t,AuthorID=auth,Publisher=pler,
                                        PublishDate=plda,Price=prc)
                return HttpResponseRedirect('/search/')
        author = Author.objects.all()
        return render_to_response('new.html',{'author':author},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login/')
    
def book_renew(request,t):
    if request.user.is_authenticated():
        if request.POST:
            b = Book.objects.get(ISBN=t)
            post = request.POST
            if post["AuthorID"] and post["Publisher"] and post['PublishDate'] and post['Price']:
                au = request.POST.get('AuthorID','')
                pler = request.POST.get('Publisher','')
                plda = request.POST.get('PublishDate','')
                prc = request.POST.get('Price','') 
                auth = Author.objects.get(id=au)
                Book.objects.filter(ISBN=t).update(Publisher=pler,AuthorID=auth,
                                        PublishDate=plda,Price=prc)
                try:
                    author = b.AuthorID
                    books = author.book_set.all()
                    q = author.Name
                    return render_to_response('search_results.html',
                                              {'books': books, 'query': q})
                except ValueError:
                    return HttpResponseRedirect('/search/')  
        authors = Author.objects.all()
        p = Book.objects.get(ISBN=t)
        q = []
        for author in authors:
            q.append(author.Name)
        return render_to_response('renew.html',locals(),context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login/')  
        
def author_add(request):
    if request.user.is_authenticated():
        if request.POST:
            post = request.POST
            if post["Name"] and post["Age"] and post["Country"]:
                na = request.POST.get('Name', '')
                age = request.POST.get('Age', '')
                cou = request.POST.get('Country', '')
                Author.objects.create(Name=na,Age=age,Country=cou)
                return HttpResponseRedirect('/book_new/')
        return render_to_response("newauthor.html",context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login/')  
     
