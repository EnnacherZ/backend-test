"""
URL configuration for storeBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from store.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/shoes/', sse_shoes, name='sse_shoes'),
    path('events/shoe_sizes/', sse_shoe_sizes, name='sse_shoe_sizes'),
    path('api/getShoes', get_shoes),
    path('api/getNewestShoes', get_newest_shoes),
    path('api/getShoeSizes', get_shoes_sizes),
    path('api/test', test),
    path('events/newest-shoes/', sse_stream_newest_shoes),
    path('api/getToken', TokenObtainPairView.as_view()),
    path('api/getToken/refresh', TokenRefreshView.as_view()),
    path('api/handlepay/', handlePayment),
    path('api/ip/', get_ip, name='get_ip'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
