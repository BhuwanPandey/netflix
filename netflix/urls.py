"""
URL configuration for netflix project.

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
import os
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    favicon_url = settings.BASE_DIR / "static/images/netflix.png"
    file = (favicon_url).open("rb")
    return FileResponse(file)


admin_name = os.getenv("ADMIN_NAME", "admin")
handler404 = 'users.views.custom_404'
urlpatterns = [
    path("favicon.ico", favicon),
    path(f'{admin_name}/', admin.site.urls),
    path("",include("users.urls"))
]
