from django.contrib import admin
from .models import Productos

@admin.register(Productos)  
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion')    
    
