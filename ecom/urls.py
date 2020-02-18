from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .api import router

urlpatterns = [ path('admin/', admin.site.urls),
path('',include('user.urls')), path('accounts/', include('allauth.urls')),
path('api-v1/',include(router.urls)),
path('api-v1/auth/',include('djoser.urls.authtoken')),
path('account/', include('social_django.urls')),
path('account/', include('django.contrib.auth.urls')),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

	