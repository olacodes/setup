from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView
# Create your views here.
from app.models import Thread

def index(request):
  threads = Thread.objects.all()
  return render(request, 'app/homepage.html', {'threads': threads})
=======

# Create your views here.
>>>>>>> 8f811f21e88cf729b6c7c9ccd17ee4f39534d193
