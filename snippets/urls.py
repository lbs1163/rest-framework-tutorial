from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('tictactoe/', views.tictactoe),
    path('users/<int:pk>/', views.user_detail),
    path('users/', views.user_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', views.snippet_list),
]
