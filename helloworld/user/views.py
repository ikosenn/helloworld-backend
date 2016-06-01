from rest_framework import viewsets

from helloworld.user.models import (
    User
)

from helloworld.user.serializers import (
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
