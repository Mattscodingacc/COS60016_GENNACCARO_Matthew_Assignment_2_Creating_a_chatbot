from django import forms

# Various form types to use in customer feedback page.

# Contact form to obtain information from user submitting their feedback.
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    phone_number = forms.CharField()
    address = forms.CharField()
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

# Form for weather_app testing.
class WeatherForm(forms.Form):
    latitude = forms.CharField(required=True)
    longitude = forms.CharField(required=True)
