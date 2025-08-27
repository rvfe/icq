# iqc_app/core/forms.py
from django import forms
from .models import PartnerApplication

class PartnerApplicationForm(forms.ModelForm):
    class Meta:
        model = PartnerApplication
        fields = [
            "company_name", "cnpj", "legal_representative", "role",
            "phone", "email", "participation_type", "message",
        ]
        widgets = {
            "company_name": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "cnpj": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "legal_representative": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "role": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "phone": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "email": forms.EmailInput(attrs={"class": "input input-bordered w-full"}),
            "participation_type": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "message": forms.Textarea(attrs={"class": "textarea textarea-bordered w-full", "rows": 4}),
        }
