from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author, Category


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20, max_length=2000)

    class Meta:
        model = Post
        fields = [
            'author',
            'choice',
            'category',
            'heading',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        text = cleaned_data.get("text")

        if heading == text:
            raise ValidationError(
                "Заголовок не может полностью совпадать с текстом статьи."
            )

        return cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'user',
        ]

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
