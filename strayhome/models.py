from django.db import models
from django.db.models import signals
# from django.utils.html import mark_safe

# Create your models here.
CAT = "CAT"
DOG = "DOG"
PET_TYPE_CHOICES = [(CAT, "кошка"), (DOG, "собака")]
MALE = "M"
FEMALE = "F"
GENDER_CHOICES = [(MALE, "мужской"), (FEMALE, "женский")]


class Breed(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    pet_type = models.CharField(max_length=3, choices=PET_TYPE_CHOICES, default=DOG, verbose_name="Вид")

    def __str__(self):
        pt = [x for x in PET_TYPE_CHOICES if x[0] == self.pet_type][0][1]
        return "%s, %s" % (self.name,  pt)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Breed, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
        ordering = ("name",)


class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Color, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Окрас"
        verbose_name_plural = "Окрасы"
        ordering = ("name",)


class Pet(models.Model):
    pet_type = models.CharField(max_length=3, choices=PET_TYPE_CHOICES, default=CAT, verbose_name="Вид")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, verbose_name="Пол")
    breed = models.ForeignKey(
        Breed, on_delete=models.CASCADE, null=True, related_name="pet_breed", verbose_name="Порода"
    )
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, related_name="pet_color", verbose_name="Окрас"
    )
    image = models.ImageField(upload_to="img/pets/", null=True, blank=True, verbose_name="Фото")
    name = models.CharField(max_length=20, verbose_name="Кличка")
    age = models.FloatField(default=0, verbose_name="Возраст, лет")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата поступления")
    sterilized = models.BooleanField(default=False, verbose_name="Стерилизовано")
    vaccinated = models.BooleanField(default=False, verbose_name="Привито")
    chipped = models.BooleanField(default=False, verbose_name="Чипировано")

    # def image_tag(self):
    #     return mark_safe('<img src="/%s" width="150" height="150" />' % (MEDIA_ROOT + self.image))
    #
    # image_tag.short_description = 'Просмотр'

    def __str__(self):
        pt = [x for x in PET_TYPE_CHOICES if x[0] == self.pet_type][0][1]
        gd = [x for x in GENDER_CHOICES if x[0] == self.gender][0][1][0:3]
        bd = str(self.breed).split(",")[0]
        return "%s, %s, %s, окрас %s, %s лет, %s" % (pt, gd, bd, self.color, self.age, self.name)

    def save(self, *args, **kwargs):
        self.age = round(abs(self.age), 2)
        return super(Pet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"
        ordering = ("pet_type", "-gender", "name", "breed__name", "color__name", "age")


# def handle_pet_file(sender, instance, created, **kwargs):
#     print(sender.id, sender.image.file)


# signals.pre_save.connect(receiver=handle_pet_file, sender=Pet)

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

@receiver(pre_save, sender=Pet)
def my_callback(sender, instance, *args, **kwargs):
    print(instance.id, instance.image.file)
    # instance.slug = slugify(instance.title)
