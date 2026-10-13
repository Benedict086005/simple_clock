from django.urls import include, path

urlpatterns = [
    # The page and the JSON time endpoint live in the "clock" app.
    path("", include("clock.urls")),
]
