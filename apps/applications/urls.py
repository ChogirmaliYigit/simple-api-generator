from django.urls import path, include
from applications.views.app import AppsListView


urlpatterns = [
    path("apps/", include([
        path("", AppsListView.as_view(), name="apps-list"),
    ]))
]
