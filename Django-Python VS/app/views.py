"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
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
def view(request):
    people = Person.objects.all()
    return render(request, "view.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()        
        tom.name = request.POST.get("name")
        tom.surname = request.POST.get("surname")
        tom.save()
    return HttpResponseRedirect("/")


# передача объектов в views.html
def view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    form = PersonForm()

    data = {
        'form':form
    }

    return render(request, 'app/view.html', data )

def layout(request):
    pn = Person.objects.all() 
    return render(request, 'app/layout.html', {'pn': pn})
