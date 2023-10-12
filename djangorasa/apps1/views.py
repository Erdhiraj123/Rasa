from django.shortcuts import render


# from .bot import agent

def home_view(request):
	return render(request, 'index.html')

