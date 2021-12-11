from django.contrib import admin
from .models import Hiretuber,Contactteam
# Register your model

class HiretuberAdmin(admin.ModelAdmin):
    list_display=('first_name','email','tuber_name','created_date')

admin.site.register(Hiretuber,HiretuberAdmin)
admin.site.register(Contactteam)