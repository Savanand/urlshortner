from django import forms

from .validators import validate_url, validate_dot_com
class SubmitUrlForm(forms.Form):
    url = forms.CharField(
            label= '',
            validators=[validate_url],
            widget= forms.TextInput(
                attrs ={
                    "placeholder":"Long URL",
                    "class": "form-control"
                }
            )
        )

    # def clean(self):   # validating on form
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     # print(cleaned_data)
    #     # print ("in clean method")
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #     return url
        # url = cleaned_data['url']  # works better as url is already is required for url line
        # print ("Printing url in clean method",url)

    # def clean_url(self):   # cleaning specific attribute working directly on field
    #     url = self.cleaned_data['url']
    #     if not "com" in url:
    #         raise forms.ValidationError("This is not valid because of no .com")
    #
    # #     # print ("in clean_url method")
    # #     # print ("Printing url in clean_url method", url)
    # #     url_validator = URLValidator()
    #
    # #     try:
    # #         url_validator(url)
    # #     except:
    # #         raise forms.ValidationError("Invalid URL")
    #     return url