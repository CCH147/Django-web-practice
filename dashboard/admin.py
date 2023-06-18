from django.contrib import admin
from .models import CountryData
from .models import City
from .models import County


# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CountyAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'name')
    
admin.site.register(CountryData)
admin.site.register(City, CityAdmin)
admin.site.register(County, CountyAdmin)