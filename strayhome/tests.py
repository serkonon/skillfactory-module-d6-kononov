from django.test import TestCase

# Create your tests here.
from strayhome.models import Pet

for Pet in Pet.objects.all():
    print(Pet.image)
