from django.contrib import admin
from strayhome.models import Breed, Pet, Color


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_filter = ("pet_type", "gender", "breed", "color")
    list_per_page = 30

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "breed":
    #         kwargs["queryset"] = Breed.objects.filter(pet_type="DOG")
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

