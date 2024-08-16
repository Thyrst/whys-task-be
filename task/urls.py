from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.views import (
    AttributeNameViewSet,
    AttributeValueViewSet,
    AttributeViewSet,
    ImageViewSet,
    ProductViewSet,
    ProductAttributesViewSet,
    ProductImageViewSet,
    CatalogViewSet,
    ImportDataViewSet,
)

router = DefaultRouter()
router.register("attribute-names", AttributeNameViewSet)
router.register("attribute-values", AttributeValueViewSet)
router.register("attributes", AttributeViewSet)
router.register("images", ImageViewSet)
router.register("products", ProductViewSet)
router.register("product-attributes", ProductAttributesViewSet)
router.register("product-images", ProductImageViewSet)
router.register("catalogs", CatalogViewSet)
router.register("import", ImportDataViewSet, basename="import")

urlpatterns = [
    path("", include(router.urls)),
]
