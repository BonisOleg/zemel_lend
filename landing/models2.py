from django.db import models
from .models1 import SingletonModel


class WorkStep(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Номер кроку')
    title = models.CharField(max_length=160, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    is_highlighted = models.BooleanField(
        default=False,
        verbose_name='Виділити золотим (Крок 4)'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Крок роботи'
        verbose_name_plural = 'Як ми працюємо (кроки)'

    def __str__(self):
        return f'Крок {self.number}: {self.title}'


class StatItem(models.Model):
    value = models.CharField(max_length=40, verbose_name='Значення')
    label = models.CharField(max_length=120, verbose_name='Підпис')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика (цифри)'

    def __str__(self):
        return f'{self.value} — {self.label}'


ICON_CHOICES = [
    ('shield', 'Щит (безпека)'),
    ('chart', 'Графік (вигода)'),
    ('clock', 'Годинник (досвід)'),
    ('key', 'Ключ (під ключ)'),
    ('eye', 'Око (моніторинг)'),
    ('checkmark', 'Галочка (гарантія)'),
    ('star', 'Зірка'),
    ('map', 'Карта'),
]


class AdvantageItem(models.Model):
    icon_key = models.CharField(
        max_length=20, choices=ICON_CHOICES, default='shield',
        verbose_name='Іконка'
    )
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Перевага'
        verbose_name_plural = 'Переваги'

    def __str__(self):
        return self.title


class AdvantagesSection(SingletonModel):
    title = models.CharField(
        max_length=120,
        default='Чому обирають «Центр Земельних Аукціонів»?',
        verbose_name='Заголовок секції'
    )
    subtitle = models.CharField(
        max_length=200,
        default='Ми знаємо ціну кожного гектара та кожної хвилини вашого часу.',
        verbose_name='Підзаголовок'
    )
    footer_quote = models.TextField(
        default=(
            'Ми працюємо на ваш результат, бо розуміємо: '
            'успішний аукціон — це початок вашого прибутку.'
        ),
        verbose_name='Цитата внизу блоку'
    )

    class Meta:
        verbose_name = 'Секція «Переваги»'
        verbose_name_plural = 'Секція «Переваги»'

    def __str__(self):
        return 'Переваги'


class ServicesSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='Які земельні ділянки ми допомагаємо продати?',
        verbose_name='Заголовок секції'
    )
    steps_title = models.CharField(
        max_length=160,
        default='Як ми працюємо: 5 кроків до успішної угоди',
        verbose_name='Заголовок блоку кроків'
    )

    class Meta:
        verbose_name = 'Секція «Послуги»'
        verbose_name_plural = 'Секція «Послуги»'

    def __str__(self):
        return 'Послуги'


class ContactSection(SingletonModel):
    title = models.CharField(
        max_length=120,
        default='Почніть свій шлях до успішної угоди вже сьогодні',
        verbose_name='Заголовок'
    )
    description = models.TextField(
        default='Ми завжди на зв\'язку, щоб обговорити вашу майбутню ділянку.',
        verbose_name='Опис'
    )
    form_title = models.CharField(
        max_length=120,
        default='Залишити заявку на безкоштовний аналіз',
        verbose_name='Заголовок форми'
    )
    form_btn_text = models.CharField(
        max_length=80,
        default='ОТРИМАТИ КОНСУЛЬТАЦІЮ ЕКСПЕРТА',
        verbose_name='Текст кнопки форми'
    )
    privacy_note = models.CharField(
        max_length=200,
        default='Ваші дані в безпеці. Ми гарантуємо повну конфіденційність кожного звернення.',
        verbose_name='Приміт. конфіденційності'
    )

    class Meta:
        verbose_name = 'Секція «Контакти»'
        verbose_name_plural = 'Секція «Контакти»'

    def __str__(self):
        return 'Контакти'


class LeadSubmission(models.Model):
    INTEREST_CHOICES = [
        ('buy', 'Купити землю'),
        ('sell', 'Продати землю'),
        ('estimate', 'Оцінка ділянки'),
    ]

    STATUS_NEW = 'new'
    STATUS_NO_ANSWER = 'no_answer'
    STATUS_CALL_BACK = 'call_back'
    STATUS_THINKING = 'thinking'
    STATUS_PUSH = 'push'
    STATUS_WAITING_PAYMENT = 'waiting_payment'

    STATUS_DATA_COLLECTION = 'data_collection'
    STATUS_IN_PROCESS = 'in_process'
    STATUS_CLOSED = 'closed'
    STATUS_OFFER_NEW = 'offer_new'

    STATUS_CHOICES = [
        (STATUS_NEW, 'Новий'),
        (STATUS_NO_ANSWER, 'Недозвон'),
        (STATUS_CALL_BACK, 'Перетелефонувати'),
        (STATUS_THINKING, 'Обдумує'),
        (STATUS_PUSH, 'Дотиснути'),
        (STATUS_WAITING_PAYMENT, 'Очікуємо оплату'),
        (STATUS_DATA_COLLECTION, 'Збір Даних'),
        (STATUS_IN_PROCESS, 'В процессі'),
        (STATUS_CLOSED, 'Закритий'),
        (STATUS_OFFER_NEW, 'Запропонувати нові послуги'),
    ]

    name = models.CharField(max_length=120, verbose_name="Ім'я")
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    interest = models.CharField(
        max_length=10, choices=INTEREST_CHOICES,
        verbose_name='Запит'
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW,
        verbose_name='Статус'
    )
    comment = models.TextField(blank=True, verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_processed = models.BooleanField(
        default=False, verbose_name='Оброблено'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.name} ({self.phone}) — {self.get_interest_display()}'


class LeadInProgress(LeadSubmission):
    class Meta:
        proxy = True
        verbose_name = 'В роботі'
        verbose_name_plural = 'В роботі'
