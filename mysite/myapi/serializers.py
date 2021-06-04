from rest_framework import serializers
from .models import Employee, Departement


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "Prenom", "Nom", "Age", "Ville", "Poste", "Salaire", "department"]


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ['Intitule', 'Etage']