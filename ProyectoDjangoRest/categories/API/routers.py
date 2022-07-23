from rest_framework.routers import DefaultRouter
from categories.API.views import CategoryApiViewSet

router_categories = DefaultRouter()

router_categories.register(prefix='categories',basename='categories',viewset=CategoryApiViewSet)