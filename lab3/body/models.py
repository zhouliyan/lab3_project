from django.db import models


class Book(models.Model):
    ISBN = models.CharField(max_length=17,primary_key = True)   #main_key
    Title =  models.CharField(max_length=100)
    AuthorID = models.ForeignKey('Author',blank = True, null = True)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Title
       
class Author(models.Model):
    Name = models.CharField(max_length = 50)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.Name
