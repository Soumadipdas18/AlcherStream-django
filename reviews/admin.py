from django.contrib import admin

# Register your models here.
from .models import Reviews,Comments
admin.site.register(Reviews)
admin.site.register(Comments)