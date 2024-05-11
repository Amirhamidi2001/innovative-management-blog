from django import forms
from article.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
