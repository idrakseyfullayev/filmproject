from django.db import models
from django.contrib.auth.models import User
from film.models import FilmModel


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    photo = models.ImageField(upload_to="accountphotos", blank=True, null=True)

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"
    
    
    

 