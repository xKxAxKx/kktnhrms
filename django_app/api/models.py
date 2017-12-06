from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class About(TimeStampedModel):
    name = models.CharField(max_length=140, blank=True)
    sub_name = models.CharField(max_length=140, blank=True)
    real_name = models.CharField(max_length=140, blank=True)
    birthday = models.DateTimeField()
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SNS(TimeStampedModel):
    name = models.CharField(max_length=140)
    account_name = models.CharField(max_length=140)
    url = models.URLField()
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=140)
    url = models.URLField()
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Inquiry(TimeStampedModel):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
