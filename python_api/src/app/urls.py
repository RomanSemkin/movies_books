from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import IMDBAPIView, OpenLibraryAPIView


app_name = "app"

urlpatterns = [
    path(
        "api/v1/token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/v1/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("api/v1/movie/", IMDBAPIView.as_view(), name="imdb"),
    path("api/v1/book/", OpenLibraryAPIView.as_view(), name="lib"),
]
