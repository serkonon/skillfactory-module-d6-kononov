from django.db import models

# Create your models here.
CAT = "CAT"
DOG = "DOG"
PET_TYPE_CHOICES = [
    (CAT, "Cat"),
    (DOG, "Dog"),
]


class Breed(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    pet_type = models.CharField(max_length=3, choices=PET_TYPE_CHOICES, default=CAT)


class Pet(models.Model):
    pet_type = models.CharField(max_length=3, choices=PET_TYPE_CHOICES, default=CAT, verbose_name="Вид")
    breed = models.ForeignKey(
        Breed, on_delete=models.CASCADE, null=True, related_name="pet_breed", verbose_name="Порода"
    )
    image = models.ImageField(upload_to="pets/", null=True, blank=True, verbose_name="Фото")
    name = models.CharField(max_length=20, verbose_name="Кличка")
    age = models.PositiveSmallIntegerField(default=0, verbose_name="Возраст")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата поступления")
    sterilized = models.BooleanField(default=False, verbose_name="Стерилизовано")
    vaccinated = models.BooleanField(default=False, verbose_name="Привито")
    chipped = models.BooleanField(default=False, verbose_name="Чипировано")
