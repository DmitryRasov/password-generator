from django.shortcuts import render
from generator_func import generator


def home(request):
	return render(request, 'index.html')


def password(request):
	thepassword = generator(request)
	return render(request, 'password.html', {'password': thepassword})
