# iqc_app/core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PartnerApplicationForm


def home(request):
    if request.method == "POST":
        form = PartnerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulário enviado com sucesso!")
            return redirect("core:home")
        messages.error(request, "Erros no formulário, confira os campos.")
    else:
        form = PartnerApplicationForm()

    whatsapp_link = "https://wa.me/5551995852380"

    return render(request, "home.html", {"form": form, "whatsapp_link": whatsapp_link})
