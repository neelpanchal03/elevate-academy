from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from school.models import School


# Register your models here.
class SchoolAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'created_on']
    search_fields = ['name']

    model = School

admin.register(School, SchoolAdmin)