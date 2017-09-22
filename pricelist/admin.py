from django.contrib import admin
from .models import Production,Service,ProductCategory,ServiceCategory

admin.site.register(Production)
admin.site.register(Service)
admin.site.register(ProductCategory)
admin.site.register(ServiceCategory)
# Register your models here.
