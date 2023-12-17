from rest_framework import routers
from .api import ProductoViewSet, MarcaViewSet, CategoriaViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/marcas', MarcaViewSet, 'marcas')
router.register('api/categorias', CategoriaViewSet, 'categorias')

urlpatterns = router.urls