from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to="book_cover", null=True, blank=True)
    pdf = models.FileField(upload_to="book_pdf", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
