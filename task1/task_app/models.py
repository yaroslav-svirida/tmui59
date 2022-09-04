from django.db import models

# Create your models here.
from django.urls import reverse

class OnlyPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(honey_token=0)

class OnlyToken(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(honey_token=1)

class Post(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)
    honey_token = models.IntegerField(default=0)
    table_name = models.TextField(default='Post')
    time_of_create = models.DateTimeField(auto_now_add=True)

    objects = OnlyPost()
    token_objects = OnlyToken()
    def __str__(self):
        return f'{self.name} - {self.id}'

    def get_absolute_url(self):
        return reverse('posts', kwargs={'pk': self.pk})

    #
    # def get_queryset(self, request):
    #     if not request.user.is_authenticated:
    # #         queryset = super().get_queryset()
    # #     # I'm not sure what the FK to user is on CoffeeOrder. I assumed customer.
    # #         queryset = queryset.filter(honey_token=1)
    # #     return queryset
    # def get_queryset(self):
    #     return Post.objects.filter(honey_token=1)


class Book(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)
    honey_token = models.IntegerField(default=0)
    table_name = models.TextField(default='Book')
    time_of_create = models.DateTimeField(auto_now_add=True)
    objects = OnlyPost()
    token_objects = OnlyToken()
    def __str__(self):
        return f'{self.name} - {self.id}'

    def get_absolute_url(self):
        return reverse('posts', kwargs={'pk': self.pk})
