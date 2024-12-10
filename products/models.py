from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    price = models.PositiveIntegerField(default=100)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    # image
    is_pay = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


