from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "users/",
        include("users.urls"),
    ),
    path(
        "news/",
        include("news.urls"),
    ),
    path(
        "tournaments/",
        include("tournaments.urls"),
    ),
    path(
        "",
        RedirectView.as_view(url="/news/"),
        name="homepage",
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
