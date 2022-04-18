from django.contrib import admin
from .models.package import Package
from .models.customer import Customer

# Register your models here.
admin.site.register(Package)
admin.site.register(Customer)