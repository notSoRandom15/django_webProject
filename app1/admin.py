from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)