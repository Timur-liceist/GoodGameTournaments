from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView

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
        "teams/",
        include("teams.urls"),
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
    path(
        "not_found",
        TemplateView.as_view(
            template_name="includes/error.html",
            extra_context={
                "error_message": "404 Not Found",
            },
        ),
        name="not_found",
    ),
    path(
        "forbidden",
        TemplateView.as_view(
            template_name="includes/error.html",
            extra_context={
                "error_message": "403 Forbidden",
            },
        ),
        name="forbidden",
    ),
    path(
        "test_tabs",
        TemplateView.as_view(
            template_name="news/test_tabs.html",
        ),
        name="test_tabs",
    ),
    path(
        "auth/",
        include(
            "social_django.urls",
            namespace="social",
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
