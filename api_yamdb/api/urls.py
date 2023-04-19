from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

v1 = DefaultRouter()
v1.register('titles', views.TitleViewSet, basename='titles')
v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews'
)
v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'r'/comments',
    views.CommentViewSet,
    basename='comments'
)
v1.register('categories', views.CategoryViewSet, basename='categories')
v1.register('genres', views.GenreViewSet, basename='genres')
v1.register('users', views.UsersViewSet, basename='users')
v1.register('auth/signup', views.AuthSignupViewSet, basename='auth_signup')
v1.register('auth/token', views.AuthTokenViewSet, basename='auth_token')

urlpatterns = [
    path('v1/', include(v1.urls)),
]
