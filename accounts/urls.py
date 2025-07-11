from django.urls import path, include
from .api import RegisterApi, LoginApi, GetUserApi
from knox import views as knox_views
urlpatterns = [
  path(
    'api/auth/register/',
    RegisterApi.as_view()
  ),
  path(
    'api/auth/login/',
    LoginApi.as_view()
  ),
  path(
    'api/auth/logout/',
    knox_views.LogoutView.as_view(),
    name = 'knox_logout'
  ),
  path(
    'api/auth/user/',
    GetUserApi.as_view()
  ),
  path(
    'api/auth/',
    include('knox.urls')
  ),
]