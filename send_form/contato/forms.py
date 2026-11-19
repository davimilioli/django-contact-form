from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=120,
        widget=forms.TextInput(attrs={
            "class": "campo-input",
            "placeholder": "Seu nome completo",
        }),
        error_messages={
            "required": "Informe o seu nome.",
        },
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "class": "campo-input",
            "placeholder": "voce@exemplo.com",
        }),
        error_messages={
            "required": "Informe o seu e-mail.",
            "invalid": "Informe um endereço de e-mail válido.",
        },
    )
    mensagem = forms.CharField(
        label="Mensagem",
        widget=forms.Textarea(attrs={
            "class": "campo-textarea",
            "rows": 4,
            "placeholder": "Escreva sua mensagem...",
        }),
        error_messages={
            "required": "Escreva uma mensagem antes de enviar.",
        },
    )

    def clean_name(self):
        name = self.cleaned_data["nome"].strip()
        if len(name < 2):
            raise forms.ValidationError("O nome deve ter pelo menos 2 caracteres")
        return name