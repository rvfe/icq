# iqc_app/core/models.py
from django.db import models

class PartnerApplication(models.Model):
    PARTICIPATION_CHOICES = [
        ("contratante_pcd", "Empresa contratante de jovem aprendiz PcD"),
        ("apoio_divulgacao", "Empresa apoiadora com recursos ou divulgação"),
        ("capacitacao_inclusao", "Empresa interessada em capacitação sobre inclusão"),
    ]

    company_name = models.CharField("Razão social", max_length=200)
    cnpj = models.CharField("CNPJ", max_length=32)
    legal_representative = models.CharField("Representante legal", max_length=120)
    role = models.CharField("Cargo", max_length=120, blank=True)
    phone = models.CharField("Telefone", max_length=50)
    email = models.EmailField("E-mail")
    participation_type = models.CharField(
        "Deseja participar como",
        max_length=32,
        choices=PARTICIPATION_CHOICES,
    )
    message = models.TextField("Mensagem (opcional)", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company_name} ({self.email})"
