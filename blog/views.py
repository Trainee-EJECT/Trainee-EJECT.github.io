from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(blogs, 3)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
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

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(title__icontains=query) | Q(author__icontains=query)
            results= Blog.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'blog/search.html', context)

        else:
            return render(request, 'blog/search.html')

    else:
        return render(request, 'blog/search.html')
