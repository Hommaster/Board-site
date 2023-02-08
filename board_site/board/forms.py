from django.forms import ModelForm
from .models import *
from django import forms


class BbForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["rubric"].empty_label = "Категория не выбрана"

    class Meta:
        model = Bb
        fields = ["title", "content", "price", "rubric", "photo"]

