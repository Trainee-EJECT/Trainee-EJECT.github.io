from django.shortcuts import render
from django.urls import reverse
from .forms import ContactMessage

# Create your views here.
def index(request):
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
	context['form'] = form
	return render(request, template_name, context)
