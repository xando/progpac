from django import forms


class Editor(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
