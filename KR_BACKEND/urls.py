from django.contrib import admin
from django.urls import path, include, re_path

from krBackend.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')), # маршрут для использования авторизации на основе сессий.
    path('api/article/', ArticleAPIListAndPost.as_view()),
    path('api/article/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('api/article_del/<int:pk>/', ArticleAPIDelete.as_view()),
    path('api/author/', AuthorAPIPost.as_view()),
    path('api/authorAdm/', AuthorAPIAdmList.as_view()),
    path('api/users/', UserAPIList.as_view()),
    path('api/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
