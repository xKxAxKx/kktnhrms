from django.contrib import admin
from api.models import About, SNS, Product, Inquiry


@admin.register(Account)
class About(admin.ModelAdmin):
    list_display = ('id')


@admin.register(Tweet)
class SNS(admin.ModelAdmin):
    list_display = ('name')


@admin.register(Follow)
class Product(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Favorite)
class Favorite(admin.ModelAdmin):
    list_display = ('tweet', 'user')


@admin.register(Reply)
class Inquiry(admin.ModelAdmin):
    list_display = ('email')
