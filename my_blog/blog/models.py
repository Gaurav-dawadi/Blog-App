from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    authorName = models.CharField(max_length=200,  null=False) 
    authorEmail = models.EmailField()
    
    def __str__(self):
        return self.authorName


class Article(models.Model):
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    articleTitle = models.CharField(max_length=100)
    articleContent = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)       
    postedTime = models.DateTimeField(default=timezone.now)
    updatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.articleTitle

    def publish(self):
        self.updatedTime = timezone.now()
        self.save()    

  
