from django.urls import include, path, re_path, reverse
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('search/', views.search, name='search'),
	re_path('(?P<slug>[\w_-]+)/', views.details, name='details'),
]