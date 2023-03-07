from django.urls import path, include
from film import views

app_name = 'film'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
    path('actor_details/<int:id>/', views.Actor_detailsView.as_view(), name='actor_details'),
    path('actors/<int:id>/', views.ActorsView.as_view(), name='actors'),
    path('film-create/', views.CreateFilmView.as_view(), name='film-create'),
    # path('fib/', views.fib),
    # path('test/', views.test),
    # path('list_intersection/', views.list_intersection),
    # path('x/', views.x),
    # path('list_intersection/', views.list_intersection),
    # path('python_prog_re_pos_neg/', views.python_prog_re_pos_neg),
    # path('movie_time/', views.movie_time),
    
]



