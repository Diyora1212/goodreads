from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField, CASCADE, ForeignKey, ManyToManyField
from apps.shared.models import AbstractModel


class User(AbstractUser):
    avatar = ImageField(upload_to='Users/avatar/%Y/%m/%d', default="default_user.png")
    middle_name = CharField(max_length=56)


class BookShelf(AbstractModel):
    name = CharField(max_length=128)
    user = ForeignKey('users.User', CASCADE, related_name='Bookshelf')
    books = ManyToManyField('books.Book', related_name='Bookshelves')

