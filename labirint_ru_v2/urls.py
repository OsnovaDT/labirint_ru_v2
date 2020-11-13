from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('books.urls')),
    path('accounts/', include('accounts.urls')),

    # For VK login
    path(
        'social/',
        include('social_django.urls', namespace='social'),
    ),

    # Debug toolbar
    path(
        '__debug__/',
        include(debug_toolbar.urls),
    ),

    # Simple captcha
    path(
        'captcha/',
        include('captcha.urls')
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
