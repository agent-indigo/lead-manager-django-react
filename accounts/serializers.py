from rest_framework.serializers import CharField, ModelSerializer, Serializer, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = (
      'id',
      'username',
      'email',
      'first_name',
      'last_name'
    )
class RegisterSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = (
      'username',
      'email',
      'password',
      'first_name',
      'last_name'
    )
    extra_kwargs = {
      'password': {
        'write_only': True
      }
    }
  def create(
    self: 'UserSerializer',
    validated_data: dict[
      str,
      object
    ]
  ) -> User:
    user = User.objects.create_user(
      **validated_data
    )
    return user
  def validate(
    self: 'RegisterSerializer',
    attrs: dict[
      str,
      object
    ]
  ) -> dict[
    str,
    object
  ]:
    if not authenticate(
      username = attrs['username'],
      password = attrs['password']
    ):
      raise ValueError('Invalid credentials')
    return attrs
class LoginSerializer(Serializer):
  username = CharField()
  password = CharField()
  def validate(
    self: 'LoginSerializer',
    data: dict[
      str,
      str
    ]
  ) -> User:
    user = authenticate(**data)
    if user and user.is_active:
      return user
    else:
      raise ValidationError(
        'Invalid credentials.'
      )