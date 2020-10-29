from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Blog

# Create your views here.
def index(request):
	blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	#blogs = Blog.objects.all()
	template_name = 'blog/index.html'
	context = {
		'blogs': blogs
	}
	return render(request, template_name, context)
def details(request, slug):
	blog = get_object_or_404(Blog, slug=slug)
	template_name = 'blog/details.html'
	context = {
		'blog' : blog
	}
	return render(request, template_name, context)