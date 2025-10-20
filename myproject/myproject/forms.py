from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(label='Restaurant Name', max_length=100)
    url = forms.URLField(label='Menu URL',max_length=100)
    color = forms.CharField(label='QR Code Color',max_length=100 , required=False,initial='#000000', widget=forms.TextInput(attrs={'type': 'color'}))

