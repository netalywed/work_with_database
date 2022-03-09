import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            id1 = int(phone["id"])
            name1 = phone["name"]
            image1 = phone["image"]
            price1 = phone["price"]
            release_date1 = phone["release_date"]
            lte1 = phone["lte_exists"]
            slug1 = slugify(name1)
            a_phone = Phone(id=id1, name=name1, image=image1, price=price1,
                            release_date=release_date1, lte_exists=lte1, slug=slug1)
            a_phone.save()

            # сразу создать запись в бд и не засорять временную память
            # a_phone = Phone.objects.create(id=id, name=name, image=image, price=price, release_date=release_date, lte_exists=lte)

        pass


