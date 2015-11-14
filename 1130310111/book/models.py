from django.db import models
from django.contrib import admin
# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length = 100)
    Name = models.CharField(max_length = 100)
    Age = models.CharField(max_length = 10)
    Country = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.Name
        
class Book(models.Model):
    class Meta:
        ordering = ['Title']
    ISBN = models.CharField(max_length = 13)
    Title = models.CharField(max_length = 100)
    AuthorID = models.CharField(max_length = 100)
    Publisher = models.CharField(max_length = 100)
    PublishDate = models.DateField()
    Price = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.Title
    

        
class BookPostAdmin(admin.ModelAdmin):
    list_display = ('ISBN','Title','AuthorID','Publisher','PublishDate','Price')
    
