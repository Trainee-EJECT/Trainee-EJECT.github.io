from django.shortcuts import render
from django.urls import reverse
from .forms import ContactMessage
from blog.models import Blog
from django.utils import timezone

# Create your views here.
def index(request):
	blog1 = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
	blog2 = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[1]
	blog3 = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[2]
	template_name = 'initial/index.html'
	context = {}
	if request.method == 'POST':
		form = ContactMessage(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactMessage()
	else:
		form = ContactMessage()
	#context['form'] = form
	context = {
		'form': form,
		'blog1': blog1,
		'blog2': blog2,
		'blog3': blog3,
	}
	return render(request, template_name, context)
