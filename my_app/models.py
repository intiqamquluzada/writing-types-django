from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader


class Product(SlugMixin, DateMixin):
    name = models.CharField(max_length=255, verbose_name="Name")
    price = models.FloatField(verbose_name="Price")
    image = models.ImageField(upload_to=Uploader.upload_images_for_products, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Product)
        super(Product, self).save(*args, **kwargs)
