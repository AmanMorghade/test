from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.shortcuts import render, redirect
from .forms import PersonForm
# Create your views here.


def tryss(request):
    return render(request,"base.html")




def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})


def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})
