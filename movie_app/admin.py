from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom  # Импортируем нашу модель
from django.db.models import QuerySet


admin.site.register(Director)
admin.site.register(Actor)
#admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class DressingRoom(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):  # делаем фильтр по рейтингу
    title = 'Фильтр по рейтингу'  # даем название в админке
    parameter_name = 'rating'  # даем название в адресной строке

    def lookups(self, request, model_admin):  # создаем метод со списком значений рейтинга
        return [
            ('<40', 'Низкий рейтинг'),
            ('от 40 до 59', 'Средний рейтинг'),
            ('от 60 до 79', 'Высокий рейтинг'),
            ('>=80', 'Высочайший рейтинг')
        ]

    def queryset(self, request, queryset: QuerySet):  # создаём метод который определяет, какой рейтинг необходим
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=79)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #exclude = ['slug']
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'year', 'director', 'rating_status'
                    ]  # Назначаем параметры которые отображаются в админке
    list_editable = ['rating', 'year', 'director',
                     ]  # Указываем значения, которые можно редактировать(Первое значение выступает в роли ссылки, его не редактируем)
    ordering = ['-rating']  # Сортировка по значению( минус это реверс)
    list_per_page = 5  # По сколько объектов отобразится на одной странице
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__istartswith', 'rating']  # делаем поисковую строку в админке
    # istartswith - i убирает чувствительность к регистру, startswith, начинает поиск только в начальных символах
    list_filter = ['name', 'currency', RatingFilter]
    filter_horizontal = ['actors']

    @admin.display(ordering='rating', description='Статус')  # ordering='rating', чтобы сортировать по значению rating
    # description='Статус' именует название столбца
    def rating_status(self, movie):  # добавляем доп значение исходя из значения рейтинга
        if movie.rating < 50:
            return 'Зачем это смотреть?'
        if movie.rating < 70:
            return 'На один раз'
        if movie.rating <= 85:
            return 'Зачёт!'
        return 'Топчик!'

    @admin.action(description='Установить валюту USD')
    def set_dollars(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'было обновлено {count_update} записей',

        )

    @admin.action(description='Установить валюту Euro')
    def set_euro(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'было обновлено {count_update} записей',

        )
