from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # path("reports/", include("apps.crawler.urls"), name="reports"),
    path("data/", include("apps.crawler.urls"), name="data"),
    path("account/", include("apps.account.urls"), name="account"),
    path("macro/", include("apps.macro.urls"), name="macro"),
]