from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reviews/<int:movie_id>/", views.review_list, name="review_list"),
    path("reviews/<int:movie_id>/add/", views.add_review, name="add_review"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
]