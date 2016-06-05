from helloworld.common.serializers import AuditFieldsMixin
from helloworld.user.models import (
    User
)


class UserSerializer(AuditFieldsMixin):
    class Meta:
        model = User
