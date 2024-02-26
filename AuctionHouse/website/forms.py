from django import forms

class AuctionSearchForm(forms.Form):
    search_query = forms.CharField(label='Search by title or address', max_length=255)