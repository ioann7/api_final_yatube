from rest_framework import viewsets
from rest_framework import filters

from posts.models import Comment, Post, Group, Follow
from api.serializers import (CommentSerializer, PostSerializer,
                             GroupSerializer, FollowSerializer)
from api.viewsets import CreateListViewSet


class FollowViewSet(CreateListViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('author__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
