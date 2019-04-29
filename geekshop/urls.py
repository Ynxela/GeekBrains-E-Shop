from django.conf.urls import url, include
from django.contrib import admin
import mainapp.views as mainapp
from django.urls import include, path, re_path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('order/', include('ordersapp.urls', namespace='order')),

    path('admin/', include('adminapp.urls', namespace='admin')),
    path('auth/verify/google/oauth2/', include("social_django.urls", namespace="social"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
