# iqc_app/core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PartnerApplicationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PartnerApplication


def home(request):
    if request.method == "POST":
        form = PartnerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulário enviado com sucesso!")
            return redirect("home")
        messages.error(request, "Erros no formulário, confira os campos.")
    else:
        form = PartnerApplicationForm()

    whatsapp_link = "https://wa.me/5551995852380"

    return render(request, "home.html", {"form": form, "whatsapp_link": whatsapp_link})


@login_required
def submissions_list(request):
    apps = PartnerApplication.objects.all().order_by("-id")
    return render(request, "submissions_list.html", {"apps": apps})