from django.shortcuts import render


def index(request):
	return render(request, 'mainApp/homepage.html')

# Create your views here.
