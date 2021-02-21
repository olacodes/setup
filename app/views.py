from django.shortcuts import render
from app.models import Thread


def index(request):
  threads = Thread.objects.all()
  return render(request, 'app/homepage.html', {'threads': threads})
