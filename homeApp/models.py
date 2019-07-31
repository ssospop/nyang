from django.db import models

class Cat(models.Model): # class명 대문자로 시작
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    

# Create your models here.
