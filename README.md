# Formulário de Contato com Django

Mini projeto em Python e Django de envio de formulário de contato. O usuário preenche nome, e-mail e mensagem, os dados são validados e, se estiverem corretos, ele é redirecionado para uma página de agradecimento.

## O que aprendi

- Criar um projeto e um app com Django
- Criar formulários com a classe `forms.Form`
- Validar campos obrigatórios e formato de e-mail
- Personalizar mensagens de erro de cada campo
- Adicionar classes e placeholders aos campos pelo `widget`
- Tratar requisições `GET` e `POST` na mesma view
- Redirecionar o usuário após o envio com `redirect`
- Organizar rotas com `path` e `include`
- Renderizar templates HTML com dados do formulário
- Guardar configurações sensíveis no `.env` com `python-decouple`

## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Crie o arquivo `.env` a partir do `.env.example` e defina uma `SECRET_KEY`
3. Execute:
   ```bash
   cd send_form
   py manage.py migrate
   py manage.py runserver
   ```
4. Acesse http://127.0.0.1:8000/, preencha o formulário e envie
5. Os dados enviados aparecem no terminal e você é levado para a página `/obrigado/`

Para adicionar ou alterar campos, edite a classe `ContatoForm` no [forms.py](send_form/contato/forms.py).

> **Obs:** por enquanto, as mensagens enviadas não são salvas no banco de dados, apenas exibidas no terminal. O salvamento no banco ainda será implementado.
