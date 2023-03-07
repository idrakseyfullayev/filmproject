from django.db import models
from django.contrib.auth.models import User
from film.models import FilmModel


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="accountphotos", blank=True, null=True)

    def __str__(self):
        return self.user.username


    
    
    

 