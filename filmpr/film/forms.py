from django import forms
from film.models import FilmModel

class FilmForm(forms.ModelForm):
    class Meta:
        model = FilmModel
        exclude = ("views_number",)

