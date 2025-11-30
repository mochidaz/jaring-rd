from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from about.models import Circle
from journal.models import Post, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'gothic-input', 'placeholder': 'Nama Kategori (contoh: Review, Lore)'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'cover_image', 'content', 'is_featured', 'is_draft']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'gothic-input', 'placeholder': 'Judul Manuskrip...'}),
            'category': forms.Select(attrs={'class': 'gothic-input'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'gothic-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'gothic-checkbox'}),
            'is_draft': forms.CheckboxInput(attrs={'class': 'gothic-checkbox'}),
            'content': CKEditorUploadingWidget(),
        }


class CircleForm(forms.ModelForm):
    class Meta:
        model = Circle
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'gothic-input'}),
            'genre': forms.TextInput(attrs={'class': 'gothic-input'}),
            'master': forms.TextInput(attrs={'class': 'gothic-input'}),
            'est_year': forms.TextInput(attrs={'class': 'gothic-input'}),
            'description': forms.Textarea(attrs={'class': 'gothic-input', 'rows': 4}),
            'key_members': forms.Textarea(attrs={'class': 'gothic-input', 'rows': 2}),
            'theme_color': forms.TextInput(attrs={'class': 'gothic-input', 'type': 'color'}),
        }
