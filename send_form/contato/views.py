from django.shortcuts import redirect, render
from . forms import ContatoForm

def send_contact(request):
    send = False
    data = None

    if request.method == "POST":
        form = ContatoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(f"Dados recebidos: {data}")
            send = True
            form = ContatoForm()
            return redirect("thank_you")
    else:
        form = ContatoForm()

    return render(
        request,
        "contato/contato.html",
        {
            "form": form,
            "send": send,
            "data": data, 
        }
    )

def thank_you(request):
    return render(request, "contato/obrigado.html")
