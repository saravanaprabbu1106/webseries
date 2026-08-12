from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def str(self):
        return self.name


class Movie(models.Model):
    MOVIE = "movie"
    WEB_SERIES = "web_series"

    CONTENT_TYPE_CHOICES = [
        (MOVIE, "Movie"),
        (WEB_SERIES, "Web Series"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movies"
    )
    content_type = models.CharField(
        max_length=20,
        choices=CONTENT_TYPE_CHOICES,
        default=MOVIE
    )
    release_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    poster = models.URLField(
        blank=True
    )

    def str(self):
        return self.title

    @property
    def average_rating(self):
        ratings = self.ratings.all()

        if not ratings.exists():
            return 0

        total = sum(rating.rating for rating in ratings)
        return round(total / ratings.count(), 1)


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movie_reviews"
    )
    review = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def str(self):
        return f"{self.user.username} - {self.movie.title}"


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movie_ratings"
    )
    rating = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "user"],
                name="unique_movie_user_rating"
            )
        ]

    def str(self):
        return f"{self.user.username} - {self.movie.title} - {self.rating}"