from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import IntegerField, CharField, TextField, ImageField, SlugField, TextChoices, URLField, \
    ManyToManyField, ForeignKey, CASCADE
from django.forms import DateField

from apps.shared.models import AbstractModel


class LanguageChoices(TextChoices):
    ENGLISH = 'en', "English"
    FRENCH = 'fr', "French"
    RUSSIAN = 'ru', "Russian"
    ARABIC = 'ar', "Arabic"
    UZBEK = 'uz', "Uzbek"


class Book(AbstractModel):
    title = CharField(max_length=128)
    slug = SlugField(unique=True)
    description = TextField()
    published = DateField()
    isbn = CharField(unique=True, max_length=50)
    language = CharField(max_length=10, choices=LanguageChoices, default=LanguageChoices.ENGLISH)
    picture = ImageField(upload_to="books/cover/%Y/%m/%d", default="default_cover.png")
    page = IntegerField()
    genre = ManyToManyField("books.BookGenre", related_name="books")
    authors = ManyToManyField("books.BookAuthor", related_name="books")


class BookAuthor(AbstractModel):
    first_name = CharField(max_length=56)
    last_name = CharField(max_length=56)
    birth_date = DateField()
    website = URLField()
    avatar = ImageField(upload_to="authors/avatars/%Y/%m/%d", default="default_author.png")
    about = TextField()


class BookGenre(AbstractModel):
    name = CharField(max_length=30)


class BookReview(AbstractModel):
    body = TextField()
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    like_count = IntegerField(default=0)
