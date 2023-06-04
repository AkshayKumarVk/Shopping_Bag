from django.contrib import admin
from eCommApp.models import productsDb, myOrderDb, contactUsDb

# Register your models here.
admin.site.register(productsDb)
admin.site.register(myOrderDb)
admin.site.register(contactUsDb)

