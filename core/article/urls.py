from django.urls import path

from article.views import HomePageView

app_name = "article"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
