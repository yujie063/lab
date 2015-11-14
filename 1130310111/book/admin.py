from django.contrib import admin
from book.models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN','Title','AuthorID','Publisher','PublishDate','Price')
    search_fields = (['Title'])
admin.site.register(Book, BookAdmin)
#admin.site.register(Book)
admin.site.register(Author)
# Register your models here.
#