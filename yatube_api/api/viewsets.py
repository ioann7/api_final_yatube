from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    """
    A viewset that provides `create` and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
