# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from myapp.models import Dreamreal #database
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from myapp.forms import LoginForm 
from books.models import Book
from books.models import Publisher

import datetime

# from mysite.forms import ContactForm    
from django.core.mail import send_mail, get_connection

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    t = get_template('login.html')
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    html = t.render({'current_date': now,'name':'WRC', 'days_of_week':daysOfWeek, 'ua': ua})
    return HttpResponse(html)

def search(request): 

    # if 'search' in request.GET:
    #     message = 'You searched for: %r' % request.GET['search']
    # else:
    #     message = 'You submitted an empty form.'
    # return HttpResponse(message)
    ##----------------------------------------------##
    # if 'q' in request.GET and request.GET['q']:
    #     q = request.GET['q']
    #     books = Book.objects.filter(title__icontains=q)
    #     return render(request, 'search_results.html',{ 'books': books, 'query': q })
    # else:
    #     return HttpResponse('Please submit a search term.')



    error = False
    if 'username' in request.GET:
        username = request.GET['username']
        email = request.GET['email']
        password = request.GET['password']
        address = request.GET['address']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']
        website = request.GET['website']
        # return HttpResponse('test',username)
        if not username:
            error = True
        elif not email:
            error = True
        elif not password:
            error = True
        elif not address:
            error = True
        elif not city:
            error = True
        elif not state:
            error = True
        elif not country:
            error = True
        elif not website:
            error = True
        else:
            foo_instance  = Publisher.objects.create(
                name=username,
                address=address,
                city=city,
                state_province=state,
                country=country,
                website=website
            )
           
            books = Book.objects.filter(title__icontains=username)
            publisher = Publisher.objects.all()
            return render(request, 'search_results.html', {'books': books, 'name': username, 'email': email, 'publisher':publisher })

    return render(request, 'login.html', {'error': error})


def registration(request) :
    now = datetime.datetime.now()
    t = get_template('registration.html')
    html = t.render({'current_date': now })
    return HttpResponse(html)

def login(request) :
    now = datetime.datetime.now()
    t = get_template('login.html')
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    html = t.render({'current_date': now,'name':'Siddhartha', 'days_of_week':daysOfWeek})
    return HttpResponse(html)

def editdetails(request,id):
    now = datetime.datetime.now()
    t = get_template('editdetails.html')
    publisher = Publisher.objects.get(id=id)
    html = t.render({'current_date': now,'publisher':publisher })
    return HttpResponse(html)

def deletedetails(request,id):
    now = datetime.datetime.now()
    t = get_template('search_results.html')
    emp = Publisher.objects.get(pk = id)
    emp.delete()
    publisher = Publisher.objects.all()
    html = t.render({'current_date': now,'publisher':publisher })
    return HttpResponse(html)

def update(request):
    _username = request.GET['username']
    _address = request.GET['address']
    _city = request.GET['city']
    _state = request.GET['state']
    _country = request.GET['country']
    _website = request.GET['website']

    if not _username:
        error = True
    elif not _address:
        error = True
    elif not _city:
        error = True
    elif not _state:
        error = True
    elif not _country:
        error = True
    elif not _website:
        error = True
    else:
        # Publisher.objects.get(id = request.GET['id']).update(name=_username,address=_address,city=_city,state_province=_state,country=_country,website=_website)

        task = Publisher.objects.get(id = request.GET['id'])
        task.name=_username,
        task.address=_address,
        task.city=_city,
        task.state_province=_state,
        task.country=_country,
        task.website=_website
        task.save()
        t = get_template('search_results.html')
        publisher = Publisher.objects.all()
        html = t.render({'publisher':publisher })
        return HttpResponse(html)




    