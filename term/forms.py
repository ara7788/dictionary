from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget = forms.TextInput(
            attrs={"placeholder": "Ваше ім'я", "class": "input-cls"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "E-mail", "class": "input-cls"}
        )
    )
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={"placeholder": "Повідомлення", "cols": 30, "rows": 9, "class": "textarea-cls"}
        )
    )