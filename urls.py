"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from django.urls import path, include
# from django.contrib import admin
from ege_django_auth_jwt.sites import ege_admin_site
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from ege_django_auth_jwt.views import jwt_logout


urlpatterns = [
    path(
        settings.URL_PATH_PREFIX,
        include(
            [
                path('logout/', jwt_logout, name='logout'),
                path('', include('cadastro_edital.urls', namespace='cadastro_edital')),
                path('', include('ege_django_auth_jwt.urls', namespace='ege_django_auth_jwt')),
                path('admin/', ege_admin_site.urls),
                # path('api-auth/', include('rest_framework.urls')),
            ]
        )
    ),
    path('', RedirectView.as_view(url=settings.LOGIN_REDIRECT_URL))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('%s__debug__/' % settings.URL_PATH_PREFIX, include(debug_toolbar.urls)))