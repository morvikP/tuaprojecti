from django.db import models
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Job(models.Model):
    title = models.CharField('Название', max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Выберите категорию")
    price = models.TextField('Плата', max_length=255)
    image = models.ImageField(upload_to='jobs_images/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title

class plan(models.Model):
    title = models.CharField('Название', max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Выберите категорию")
    price = models.TextField('Плата', max_length=255)
    image = models.ImageField(upload_to='jobs_images/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "дизайн"
        verbose_name_plural = "дизайны"

    def __str__(self):
        return self.title
    
class deli(models.Model):
    title = models.CharField('Название', max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Выберите категорию")
    price = models.TextField('Плата', max_length=255)

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"

    def __str__(self):
        return self.title
    
class vak(models.Model):
    title = models.CharField('Название', max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Выберите категорию")
    price = models.TextField('Плата', max_length=255)
    image = models.ImageField(upload_to='jobs_images/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Вансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title