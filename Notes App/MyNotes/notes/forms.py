from django import forms
from .models import Note

class NotesForm(forms.ModelForm): # clasa bazata pe clasa ModelForm din Django
    class Meta: # nested class ofera metadata pentru formular adica modelul asociat si field-urile
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3', 'placeholder': '(ु⁎ᴗ_ᴗ⁎)ु.｡oO', 'style': 'font-style: italic; color: #555; border-color: pink;'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3', 'rows': 4, 'placeholder': '(ु⁎ᴗ_ᴗ⁎)ु.｡oO', 'style': 'font-style: italic; color: #555; border-color: pink;'}),
        }
        labels = {
            'title': 'Titlul Notiței',
            'text': 'Conținutul Notiței',
        }

