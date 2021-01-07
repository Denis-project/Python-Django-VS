"""
Definition of views.
"""
from django.views.generic.list import ListView
from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect

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

# получение данных из бд
def view(request):
    people = Person.objects.all()
    return render(request, "app/view.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.surname = request.POST.get("surname")
        tom.save()
    return HttpResponseRedirect("/")