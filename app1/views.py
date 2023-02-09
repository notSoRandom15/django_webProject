from datetime import datetime
from random import randint
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from firstDjangoProject.app1.models import Actor

from .datasource import get_actors, get_employees

# Create your views here.

def homePageView(request):
    return HttpResponse(f'''
        <html>
            <h1>Hello from python code!</h1> {datetime.now()}
        </html>''')
    

def homePageTempalate(request):
    return render(request, "home.html" , context = {
        'title':'Home Page Title',
        'numbers': list(range(1,randint(5,11))),
        'employees': get_employees(20),
        'now':datetime.now()
        })
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ActorsPageView(TemplateView):
    
    # template_name: str = 'actors.html'
    
    # a = Actor()
    # a.first_name = "John"
    # a.last_name = "Smith"
    # a.birth_date = datetime.now()    
    # a.save()
    
    # all = Actor.objects.all()
    # b = Actor.objects.get(pk = 1)
    # b.first_name = "another"
    # b.save()
    
    def get_context_data(self):
        context = super().get_context_data()
        context["actors"] = get_actors()
        return context
    