from django import forms

# our new form
class ContactForm(forms.Form):
    Nome = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Assunto = forms.CharField(required=True)
    Mensagem = forms.CharField(
        required=True,
        widget=forms.Textarea
    )