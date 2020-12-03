"""
Definition of views.
"""

from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render
from .forms import PersonForm
from .models import Person


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def view(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/view.html',
        {
            'title':'View',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

# БД 
# получение данных из бд
def Person_list(request):
    persons = Person.objects.all()
    return render(request, "tamplates/view.html", context = {'persons': persons})
 


# передача объектов в views.html
def Person_list(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    form = PersonForm()

    data = {
        'form':form
    }

    return render(request, 'app/view.html', data )


