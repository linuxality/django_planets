from django.shortcuts import render
from .models import Planets

# Create your views here.
def index(request):
    planets = Planets.objects.all()
    return render(request, 'index.html', {'planets':planets})
