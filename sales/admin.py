from django.contrib import admin

from .models import User, sale, Sales_Agent


admin.site.register(User)
admin.site.register(sale)
admin.site.register(Sales_Agent)
