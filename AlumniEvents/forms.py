from django import forms
from tinymce.widgets import TinyMCE
from datetime import datetime

from django import forms
from .models import Event
from tinymce.widgets import TinyMCE

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'body', 'start_date', 'end_date', 'location']
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }


    