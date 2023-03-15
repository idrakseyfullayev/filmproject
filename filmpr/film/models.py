from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActorModel(models.Model):
    poster = models.ImageField(upload_to='posters/')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    about = models.TextField()
    

    class Meta:
        verbose_name = "Actor"

    @property
    def fullname(self):
        return self.name + " " + self.surname

    def __str__(self) -> str:
        return self.name + " " + self.surname



class FilmModel(models.Model):
    poster = models.ImageField(upload_to='posters/')
    video = models.FileField(upload_to='films/')
    views_number = models.IntegerField(default=0)
    name = models.CharField(max_length=256, help_text="zehmet olmasa simbol daxil edin")
    rating = models.FloatField(default=0)
    pub_date = models.DateField()
    about = models.TextField()
    actors = models.ManyToManyField(ActorModel, related_name= "films")
    

    class Meta:
        verbose_name = "Film"
    
    def __str__(self) -> str:
        return self.name


class LikeModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.user.username + "|" + self.film.name    


class CommentModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField()
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("-id",)


    def __str__(self):
        return self.user.username + "|" + self.film.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    films = models.ManyToManyField(FilmModel, related_name="film_categories")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ViewNumberModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_viewnumbers")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_viewnumbers")

    class Meta:
        verbose_name = "View number"
        verbose_name_plural = "View numbers"

    def __str__(self):
        return self.user.username + "|" + self.film.name
    

   








