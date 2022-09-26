from django import forms


class BuySellForm(forms.Form):
    amount = forms.FloatField(min_value=0.0)
