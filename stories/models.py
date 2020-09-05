from django.db import models
from django.urls import reverse

# Create your models here.
class Stories(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  view = models.IntegerField(default=0)
  slug = models.SlugField(null=True, unique=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('story', kwargs={'slug': self.slug})
  