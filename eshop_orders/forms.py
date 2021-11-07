
from django import forms



class UserNewOrderFom(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    count = forms.IntegerField(widget=forms.NumberInput(),initial=1,min_value=1)