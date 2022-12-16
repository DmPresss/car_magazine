from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100,  db_index=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Car(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Make and model of car ")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        default=True, verbose_name="Publication")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    cat = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Category")

    def __str__(self):
        return self.title
# Car.objects.all()
# <QuerySet [<Car: Toyota>, <Car: Subaru>, <Car: Mitsubishi>, <Car: lada>, <Car: BMW>]>

    class Meta:
        verbose_name = "All car"
        ordering = ['-time_create']
