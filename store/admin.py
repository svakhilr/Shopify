from django.contrib import admin
from .models import Product,Category,Variation




class Productadmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock' , 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}
    


class Variationadmin(admin.ModelAdmin):
    list_display= ('product','variation_category','variation_value','is_active','created_date')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value',)

class Catogoryadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}
    list_display = ("category_name","slug",)

admin.site.register(Category,Catogoryadmin)

admin.site.register(Product,Productadmin)
admin.site.register(Variation,Variationadmin)
