from django.contrib import admin

from apps.books.models import Book, BookAuthor, BookGenre, BookReview
from apps.users.models import User, BookShelf

admin.site.register([BookAuthor, BookGenre, BookReview])


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register([User, BookShelf])
