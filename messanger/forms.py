from django import forms
from .models import Message

        
class Compose_Message(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body', 'recipient')
        