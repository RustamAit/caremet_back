from django.contrib import admin

# Register your models here.
from helperRequestApi.models import Helper, HelperRequest

admin.site.register(Helper)
admin.site.register(HelperRequest)
