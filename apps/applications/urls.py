from applications.views.app import AppsListView
from django.urls import include, path

urlpatterns = [
    path(
        "apps/",
        include(
            [
                path("", AppsListView.as_view(), name="apps-list"),
            ]
        ),
    )
]
