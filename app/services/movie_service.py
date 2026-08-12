from app.models.models import Movie


def get_all_movies():
    return Movie.objects.all().order_by(
        "-release_year",
        "title"
    )


def get_movie(movie_id):
    return Movie.objects.filter(
        id=movie_id
    ).first()