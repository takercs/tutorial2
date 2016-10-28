"""tutorial2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from tutorial2 import views as tutorial2_views
from newsletter import views as newsletter_views

urlpatterns = [
    url(r'^$', tutorial2_views.cover, name='cover'),
    url(r'^contact/', newsletter_views.contact, name='contact'),
    url(r'^home/', newsletter_views.home, name='home'),
    url(r'^about/', tutorial2_views.about, name='about'),
    url(r'^work/', tutorial2_views.work, name='work'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    """urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""
