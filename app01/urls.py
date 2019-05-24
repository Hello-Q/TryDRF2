"""TryDRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app01 import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

# book_list = views.BookViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# book_detail = views.BookViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
# router = DefaultRouter()
# router.register('book', views.BookViewSet)
# router.register('publisher', views.publisher_list)

# schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    # path('', include(router.urls)),
    # path('schema/', schema_view),
    # path('docs/', include_docs_urls(title='图书管理系统')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', views.api_root),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
    # path('book/', book_list, name='book-list'),
    # path('book/<pk>/', book_detail, name="book-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
