from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse


class Author(models.Model):
    user = models.CharField(max_length=40, unique=True)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        post_rating = self.post_set.all().aggregate(postRating=Sum('rating'))
        pr = 0
        pr += post_rating.get('postRating')

        comment_rating = self.user.comment_set.all().aggregate(commentRating=Sum('rating'))
        cr = 0
        cr += comment_rating.get('commentRating')

        self.rating = pr * 3 + cr
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def get_absolute_url(self):
        return reverse('post_list')


class Post(models.Model):
    choices = {
        "N": "Новость",
        "S": "Статья"
    }
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=choices)
    time_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating += 1
        self.save()

    def preview(self):
        return f"{self.text[:124]}..."

    def get_absolute_url(self):
        return reverse('post_list')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating += 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

