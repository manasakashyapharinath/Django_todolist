from django import forms 

class FormCheck(forms.ModelForm):
    checked = forms.BooleanField()

    class Meta:
        model = todos
