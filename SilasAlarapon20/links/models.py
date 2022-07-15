from django.db import models
from django.contrib.auth import get_user_model

from SilasAlarapon20.links.managers import ActiveLinkManager
# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author =models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active =models.BooleanField(True)
    objects = models.Manager()
    public = ActiveLinkManager()