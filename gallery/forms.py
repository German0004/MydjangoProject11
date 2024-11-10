from django import forms
from .models import Picture
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ["title", "image"]  # Вказуємо поля, які потрібно відобразити у формі

    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
        
        # Initialize the Crispy Forms helper
        self.helper = FormHelper()
        
        # Define form layout
        self.helper.layout = Layout(
            'title',
            'image',
            Submit('submit', 'Save', css_class='btn btn-primary')
        )