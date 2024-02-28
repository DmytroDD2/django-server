"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularSwaggerView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from my_model.views import MyModelItemViewSet

# Define the router before using it in urlpatterns
router = DefaultRouter(trailing_slash=False)
router.register('my-model', MyModelItemViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [

    path("admin/", admin.site.urls),
    path("my-model/", include("my_model.urls")),
    path('schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Додано префікс `/api/v1/` до всіх URL-адрес API
    path('api/v1/', include(router.urls)),
    path('', RedirectView.as_view(url='api/v1/docs/')),

]
urlpatterns += staticfiles_urlpatterns()