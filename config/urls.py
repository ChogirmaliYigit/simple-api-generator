import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Rest API generator",
        default_version="v1",
        description="The description",
        contact=openapi.Contact(email="chogirmali.yigit@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path(
        "api/",
        include(
            [
                path(
                    "schema/",
                    include(
                        [
                            path(
                                "swagger",
                                schema_view.with_ui("swagger", cache_timeout=0),
                                name="schema-swagger-ui",
                            ),
                            path(
                                "redoc",
                                schema_view.with_ui("redoc", cache_timeout=0),
                                name="schema-redoc",
                            ),
                        ]
                    ),
                ),
                path(
                    "v1/",
                    include(
                        [
                            path("users/", include("users.urls")),
                            path("apps/", include("applications.urls")),
                            path(
                                "app/",
                                include(
                                    [
                                        path("shop/", include("shop.urls")),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
