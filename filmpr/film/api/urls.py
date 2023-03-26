from django.urls import path
from film.api import views

app_name = 'film'

urlpatterns = [
    path('actors/', views.ActorModelListAPIview.as_view(), name='actors'),
    path('actor-create/', views.ActorModelCreateAPIView.as_view(), name="actor-create"),
    path('actor-update/<int:id>/', views.ActorModelUpdateAPIView.as_view(), name="actor-update"),
    path('actor-destroy/<int:id>/', views.ActorModelDestroyAPIView.as_view(), name="actor-destroy"),
    path('films/', views.FilmModelListAPIView.as_view(), name="films"),
    path("film-create/", views.FilmModelCreateAPIView.as_view(), name="film-create"),
    path('film-update/<int:id>/', views.FilmModelUpdateAPIView.as_view(), name="film-apdate"),
    path('film-destroy/<int:id>/', views.FilmModelDestroyAPIView.as_view(), name="film-destroy"),
    path('likes/', views.LikeModelListAPIView.as_view(), name="likes"),
    path("like-create/", views.LikeModelCreateAPIView.as_view(), name="like-create"),
    path('like-update/<int:id>/', views.LikeModelUpdateAPIView.as_view(), name="like-apdate"),
    path('like-destroy/<int:id>/', views.LikeModelDestroyAPIView.as_view(), name="like-destroy"),
    path('comments/', views.CommentModelListAPIView.as_view(), name="comments"),
    path("comment-create/", views.CommentModelCreateAPIView.as_view(), name="comment-create"),
    path('comment-update/<int:id>/', views.CommentModelUpdateAPIView.as_view(), name="comment-apdate"),
    path('comment-destroy/<int:id>/', views.CommentModelDestroyAPIView.as_view(), name="comment-destroy"),
    path('categories/', views.CategoryModelListAPIView.as_view(), name="categories"),
    path("category-create/", views.CategoryModelCreateAPIView.as_view(), name="category-create"),
    path('category-update/<int:id>/', views.CategoryModelUpdateAPIView.as_view(), name="category-apdate"),
    path('category-destroy/<int:id>/', views.CategoryModelDestroyAPIView.as_view(), name="category-destroy"),
    path('viewnumbers/', views.ViewNumberModelListAPIView.as_view(), name="viewnumbers"),
    path("viewnumber-create/", views.ViewNumberModelCreateAPIView.as_view(), name="viewnumber-create"),
    path('viewnumber-update/<int:id>/', views.ViewNumberModelUpdateAPIView.as_view(), name="viewnumber-apdate"),
    path('viewnumber-destroy/<int:id>/', views.ViewNumberModelDestroyAPIView.as_view(), name="viewnumber-destroy"),
]