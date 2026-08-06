from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def str(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    rating = models.IntegerField(default=1)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.username}-{self.movie.title}"

