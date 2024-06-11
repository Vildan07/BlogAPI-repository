from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, PostViewSet, CommentViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)
router.register('like', LikeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]