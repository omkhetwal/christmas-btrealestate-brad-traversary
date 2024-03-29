from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/',include('listings.urls')),
    path('', include('pages.urls')),
    path('',include('contacts.urls')),
    path('accounts/',include('accounts.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


