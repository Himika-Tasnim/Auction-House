from django import forms
from .models import AuctionItem
from django.forms.widgets import TimeInput

class AuctionSearchForm(forms.Form):
    search_query = forms.CharField(label='Search by title or address', max_length=255)

class AuctionItemForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = ['title', 'description', 'address', 'start_price', 'start_time', 'end_time', 'image']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }