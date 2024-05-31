from django.contrib import admin
from . models import Event
from django import forms
from tinymce.widgets import TinyMCE

# Register your models here.
class EventAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

    list_display=('title','start_date','end_date','location')
    list_filter=('title','start_date','end_date','location')
    search_fields=('title','start_date','end_date','location')
    
    
admin.site.register(Event,EventAdmin)