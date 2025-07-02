from django.contrib import admin
from .models import OrganicChemistry
from .models import PhysicalChemistry
from .models import Physics
from .models import InorganicChemistry
from .models import Mathematics

admin.site.register(OrganicChemistry)
admin.site.register(PhysicalChemistry)
admin.site.register(Physics)
admin.site.register(InorganicChemistry)
admin.site.register(Mathematics)

