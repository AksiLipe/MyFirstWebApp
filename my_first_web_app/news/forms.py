from .models import articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class articlesForm(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новости'}),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'}),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'}),
        }
