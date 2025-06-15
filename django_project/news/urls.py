from django.urls import path

import news.views

app_name = "news"

urlpatterns = [
    path(
        "",
        news.views.AllGeneralNewsView.as_view(),
        name="general_news",
    ),
    path(
        "create",
        news.views.CreateGeneralNewsView.as_view(),
        name="create_news",
    ),
    path(
        "<int:news_id>/edit",
        news.views.EditGeneralNewsView.as_view(),
        name="edit_news",
    ),
]
