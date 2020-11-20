from django.contrib import admin
from strayhome.models import Breed, Pet

# Register your models here.
@admin.register(Breed)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PublisherAdmin(admin.ModelAdmin):
    pass