"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from categories.API.routers import router_categories
from post.API.routers import router_post
from comments.API.routers import router_comments

schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion API",
        default_version='v1',
        description="Api SuservicioBoyaca",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cardenashenryesteban@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,

)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # Rutas registro usuario
                  path('api/', include('users.API.routers')),
                  # Rutas Categorias
                  path('api/', include(router_categories.urls)),
                  # Rutas Posts
                  path('api/', include(router_post.urls)),
                  # Rutas comentarios
                  path('api/', include(router_comments.urls)),

                  # Rutas documentacion API
                  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
