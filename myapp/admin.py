from django.forms import ModelForm
from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'image_tag')

    def image_tag(self, obj):
        return format_html('<img src="{0}" style="width: 450px; height:300px;" />'.format(obj.image.url))


admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(CartProduct)



