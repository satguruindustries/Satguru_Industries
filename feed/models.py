from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# for image compression
from io import BytesIO
from PIL import Image
from django.core.files import File

#image compression method
def compress(image):
    im = Image.open(image)
    im = im.convert('RGB')
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image

class Product(models.Model):
    name = models.CharField(max_length=255)
    hsn = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    cgst = models.DecimalField(max_digits=5, decimal_places=2)
    sgst = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class invoice(models.Model):
    cust_name = models.CharField(max_length=255, blank=False)
    cust_add = models.CharField(max_length=255, blank=False)
    cust_place = models.CharField(max_length=255, blank=False)
    cust_gstin = models.CharField(max_length=255, blank=False)
    invoice_num = models.CharField(max_length=20, unique=True)
    date = models.CharField(max_length=255, blank=False)
    products = models.ManyToManyField(Product, through='InvoiceItem')
    freight_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)

    def __str__(self):
        return str(self.invoice_num)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.invoice.invoice_num) + " - " + self.product.name


class Stock(models.Model):
    date = models.CharField(max_length=255, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transfer = models.IntegerField()

    def __str__(self):
        return self.product.name + " - " + self.date

class SellStock(models.Model):
    date = models.CharField(max_length=255, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name + " - " + self.date