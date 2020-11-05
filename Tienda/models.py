from django.db import models

class Producto(models.Model):
    IDP = models.AutoField(db_column='IDP', primary_key=True)
    Codigo = models.CharField(db_column='Codigo',max_length=30, blank=False, null=False)
    Nombre = models.CharField(db_column='Nombre',max_length=30, blank=False, null=False)
    Descripcion = models.CharField(db_column='Descripcion',max_length=1000, blank=False, null=False)
    Precio_de_venta = models.IntegerField(db_column='Precio_de_venta', blank=False, null=False)
    URL_Video = models.CharField(db_column='URL_Video',max_length=1000, blank=False, null=True)
    URL_Imagen = models.CharField(db_column='URL_Imagen',max_length=1000, blank=False, null=True)
        
    class Meta:
        managed = False
        db_table = 'producto'