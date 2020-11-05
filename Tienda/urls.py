from django.urls import path
from django.conf.urls import url, handler404, handler500
from .views import index, ProductoList, ProductoCreate, ProductoDelete, ProductoUpdate, ProductoView
from django.contrib.auth.decorators import login_required
from Tienda.views import RegistrarUsuario

urlpatterns = [
    path('',login_required(index)),
    path('agregar_producto',login_required(ProductoCreate.as_view())),
    path('consultar_producto',login_required(ProductoList.as_view()),name = 'ver_producto'),
    url(r'^modi_producto/(?P<pk>\d+)/$',login_required(ProductoUpdate.as_view()),name = 'modi_produc'),
    url(r'^elim_producti/(?P<pk>\d+)/$',login_required(ProductoDelete.as_view()), name= 'eli_produc'),  
    path('view/<int:pk>', ProductoView.as_view(),name='view_produc'),
    path('crear_usuario',RegistrarUsuario.as_view()),
    ]
