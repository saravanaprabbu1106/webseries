from django.contrib import admin

from app.models.models import (
    Genre,
    Movie,
    Review,
    Rating
)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content_type",
        "genre",
        "release_year"
    ]

    list_filter = [
        "content_type",
        "genre",
        "release_year"
    ]

    search_fields = [
        "title",
        "description"
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "movie",
        "user",
        "created_at"
    ]

    search_fields = [
        "movie__title",
        "user__username"
    ]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "movie",
        "user",
        "rating"
    ]

    list_filter = ["rating"]