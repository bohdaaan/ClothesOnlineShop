from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    main_image = models.ImageField(upload_to='images/', blank=False)
    color = models.CharField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images/')


class ProductSize(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.size.name} ({self.stock} in stock) for {self.product.name}"

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


