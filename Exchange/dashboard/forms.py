from django import forms


class BuyForm(forms.Form):
    amount = forms.FloatField(min_value=0.0)


class SellForm(forms.Form):
    amount = forms.FloatField(min_value=0.0)
