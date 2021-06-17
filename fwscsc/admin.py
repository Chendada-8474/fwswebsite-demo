from django.contrib import admin
from .models import Supplier
from .models import Accessories
from .models import TrailCamBrand
from .models import TrailCamPro
from .models import Recruitment
from .models import Department

admin.site.register(Supplier)
admin.site.register(TrailCamBrand)
admin.site.register(Accessories)
admin.site.register(TrailCamPro)
admin.site.register(Recruitment)
admin.site.register(Department)
# Register your models here.
