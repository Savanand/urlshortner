from django import forms

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label= 'submit URL')