from django import forms


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    image = forms.ImageField()
