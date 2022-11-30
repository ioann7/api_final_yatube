from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
