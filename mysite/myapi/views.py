from django.shortcuts import render

from rest_framework import viewsets

from .serializers import EmployeeSerializer, DepartementSerializer
from .models import Employee, Departement


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by("Nom")
    serializer_class = EmployeeSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all().order_by("Intitule")
    serializer_class = DepartementSerializer