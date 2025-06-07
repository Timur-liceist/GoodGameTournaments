from django.urls import path

import news.views

app_name = "news"

urlpatterns = [
    path(
        "",
        news.views.AllNewsView.as_view(),
        name="general_news",
    ),
    path(
        "create",
        news.views.CreateNewsView.as_view(),
        name="create_news",
    ),
]
