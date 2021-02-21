from django.shortcuts import render
from app.models import Thread, User


def index(request):
  threads = Thread.objects.all()
  users = User.objects.all()
  return render(request, 'app/homepage.html', {'threads': threads, 'users': users})
