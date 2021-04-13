from django import forms
from .models import EmployeesTable

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeesTable
        fields=['firstName','lastName','email','phone','DOB','img']