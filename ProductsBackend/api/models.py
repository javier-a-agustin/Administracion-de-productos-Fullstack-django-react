from django.db import models

# Create your models here.

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
