from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
	author = models.CharField('Autor', max_length=100)
	title = models.CharField('Título', max_length=200)
	slug = models.SlugField('Atalho')
	text = models.TextField('Texto')
	image = models.ImageField(upload_to='blog/images', verbose_name='Imagem',
		null=True, blank=True 
	)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:details', args=[str(self.slug)])

	class Meta:
		verbose_name = 'Blog'
		verbose_name_plural = 'Blogs'
		ordering = ['created_date']