from django.db import models


# def images_path():
#     return os.path.join(settings.LOCAL_FILE_DIR, 'images')
#
# class MyModel(models.Model):
#     file = models.FilePathField(path=images_path)

class Phone(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return f'{self.name}'

