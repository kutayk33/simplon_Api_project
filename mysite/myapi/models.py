from django.db import models

# from django.db.models.query import prefetch_related_objects


class Departement(models.Model):
    Intitule = models.CharField(max_length=100, primary_key=True)
    Etage = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.Intitule


class Employee(models.Model):
    Prenom = models.CharField(max_length=10, null=False, blank=False)
    Nom = models.CharField(max_length=10, null=False, blank=False)
    Age = models.SmallIntegerField(default=30)
    Ville = models.CharField(max_length=100, default="Paris")
    Poste = models.CharField(max_length=100)
    Salaire = models.DecimalField(
        max_digits=10, decimal_places=2, default=30000, blank=False, null=False
    )
    department = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Prenom} {self.Nom}"
