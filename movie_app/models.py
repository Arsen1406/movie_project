from django.db import models
from django.urls import reverse
from django.utils.text import slugify  # метод создания slug - slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100, default='Торантино')
    last_name = models.CharField(max_length=100, default='Квентин')
    direktor_mail = models.EmailField(default='no@gmail.com')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Movie(models.Model):  # Создаем модель наших данных
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    name = models.CharField(max_length=40)  # Строковое значение CharField
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])  # Числовое значение IntegerField
    year = models.IntegerField(null=True, blank=True)  # null=True - при создании это поле можно не заполнять
    # blank=True - в поле можно установить пустое значение
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)])  # default=1000000 стандартное значение
    slug = models.SlugField(default='', null=False,
                            db_index=True)  # колонка slug для отображение понятного имени в адресной строке

    # Например Dark Knight, будет dark-knight.

    def save(self, *args, **kwargs):  # Это функция которая задает slug для данных
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}% - {self.year} - {self.budget}{self.currency}'

# from movie_app.models import Movie
# Movie.objects.all()
# from django.db.models import Q
