from django import forms

# Form for chatbot data capture.
class ChatBotForm(forms.Form):
    question = forms.CharField(required=True)