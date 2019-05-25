from django.db import models
from datetime import datetime
from PIL import Image
# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    added_at = models.DateTimeField(default=datetime.now, blank=True)
    #image = models.ImageField(upload_to='', blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.name + ' - ' + self.category
    class Meta:
        verbose_name_plural = "Product"
