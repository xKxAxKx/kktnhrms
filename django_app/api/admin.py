from django.contrib import admin
from api.models import About, SNS, Product, Inquiry


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(SNS)
class SNS(admin.ModelAdmin):
    list_display = ('order', 'name', 'url',)
    ordering = ('order',)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Inquiry)
class Inquiry(admin.ModelAdmin):
    list_display = ('email',)
