from django.urls import include, path
from . import views

app_name = 'initial'

urlpatterns = [
	path('', views.index, name='index'),
]