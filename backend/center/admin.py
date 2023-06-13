from django.contrib import admin
from .models import center, owner, registration, inspection, account

admin.site.register(center)
admin.site.register(owner)
admin.site.register(registration)
admin.site.register(inspection)
admin.site.register(account)