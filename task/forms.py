from django import forms 
from .models import Product

class Add_Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price','quantity']
        widgets = {'product_name':forms.TextInput(attrs={'class':'form-control'}),'price':forms.NumberInput(attrs={'class':'form-control','max_length':'10'}), 'quantity':forms.NumberInput(attrs={'class':'form-control'})}