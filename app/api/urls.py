from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "movie/<int:movie_id>/",
        views.movie_detail,
        name="movie_detail"
    ),

    path(
        "reviews/<int:movie_id>/",
        views.review_list,
        name="review_list"
    ),

    path(
        "reviews/<int:movie_id>/add/",
        views.add_review,
        name="add_review"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]