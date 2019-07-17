from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


# admin.site.register(Author)

admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
