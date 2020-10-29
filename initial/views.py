from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
	template_name = 'initial/index.html'
	return render(request, template_name)
