from django.contrib import admin
from .models import Worker, Consumer, Mechanic
# Register your models here.

admin.site.register(Worker)
admin.site.register(Consumer)
admin.site.register(Mechanic)
