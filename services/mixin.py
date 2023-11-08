from django.db import models


class SlugMixin(models.Model):
    slug = models.SlugField(verbose_name="Slug", unique=True, editable=False)

    class Meta:
        abstract = True


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
