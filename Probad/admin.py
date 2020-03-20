from django.contrib import admin
from .models import *

admin.site.register(Division)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Resturant)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','name','bn_name','division']


admin.site.register(District, DistrictAdmin )

class ChondokothaAdmin(admin.ModelAdmin):
    list_display = ['title','category','district','category_name','district_name','division_name']


admin.site.register(Chondokotha )



