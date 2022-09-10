from django.contrib import admin
from mng_app.models import Department,Role,Employee
# Register your models here.

admin.site.register((Department,Role,Employee))