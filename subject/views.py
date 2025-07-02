from django.shortcuts import render
from .models import PhysicalChemistry, Physics, Mathematics, InorganicChemistry, OrganicChemistry


def jee(request):
    data_physical_chemistry = PhysicalChemistry.objects.all()
    data_organic_chemistry = OrganicChemistry.objects.all()
    data_physical = Physics.objects.all()
    data_mathematics = Mathematics.objects.all()
    data_inorganic_chemistry = InorganicChemistry.objects.all()
    return render(request, 'subject/jee.html',
                  {'physical': data_physical_chemistry, 'organic_chemistry': data_organic_chemistry,
                   'inorganic_chemistry': data_inorganic_chemistry, 'physic': data_physical,
                   'mathematics': data_mathematics})
