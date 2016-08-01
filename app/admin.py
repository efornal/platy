from django.contrib import admin
from app.models import Institute
from app.models import Doctype
from app.models import Career
from app.models import Order
from app.models import User

# # Register your models here.
admin.site.register(Institute)
admin.site.register(Doctype)
admin.site.register(Career)
admin.site.register(Order)
admin.site.register(User)
