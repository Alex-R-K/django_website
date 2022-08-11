from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200)  # "required=False" make form's field optional |||| wiget=forms.TextInput(
    # attrs={'class':'css.input'}))
    phone = forms.CharField(max_length=200)
    # go to views.py
