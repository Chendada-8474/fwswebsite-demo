from django.contrib import admin
from .models import Supplier
from .models import Accessories
from .models import Brands
from .models import TrailCamPro

admin.site.register(Supplier)
admin.site.register(Brands)
admin.site.register(Accessories)
admin.site.register(TrailCamPro)
# Register your models here.
