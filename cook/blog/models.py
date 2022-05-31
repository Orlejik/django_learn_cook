from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
                            'self', 
                            related_name='children', 
                            on_delete=models.SET_NULL, 
                            blank=True, 
                            null=True
                            )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tags'

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'articles/')
    text = models.TextField()
    category = models.ForeignKey(
                                Category, 
                                related_name='post', 
                                on_delete=models.SET_NULL, 
                                null=True
                                )
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'author']
        verbose_name_plural = 'Posts'

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingridients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post, 
        related_name='recipe', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Recipes'

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(
        Post, 
        related_name='comment', 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Comments'



