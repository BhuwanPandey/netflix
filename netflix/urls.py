import os
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET
from django.conf.urls.static import static

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    favicon_url = settings.BASE_DIR / "static/images/netflix.png"
    file = (favicon_url).open("rb")
    return FileResponse(file)

# this work on debug = false
handler404 = 'users.views.custom_404'
admin_site = os.getenv("admin_site", "admin")
urlpatterns = [
    path("favicon.ico", favicon),
    path(f'{admin_site}/', admin.site.urls),
    path("",include("users.urls")),
    path("",include("movies.urls")),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
