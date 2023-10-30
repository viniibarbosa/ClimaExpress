from django import forms

class ClimaForms(forms.Form):
    cidade = forms.CharField(
        label = "Cidade",
        required = True,
        widget = forms.TextInput(
            attrs={
                "class" : "form",
                "placeholder": "Digite uma cidade"
            }
        )
    )