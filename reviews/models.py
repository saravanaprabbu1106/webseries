from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def str(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user.username} - {self.movie.title}"


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def str(self):
        return f"{self.user.username} - {self.movie.title} - {self.rating}"