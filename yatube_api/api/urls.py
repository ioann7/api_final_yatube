from django.urls import path, include
from rest_framework import routers

from api.views import GroupViewSet, FollowViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
