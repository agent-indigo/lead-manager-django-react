from urllib.request import Request
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
class RegisterApi(GenericAPIView):
  serializer_class = RegisterSerializer
  def post(
    self: 'RegisterApi',
    request: Request,
    *args: tuple,
    **kwargs: dict[
      str,
      object
    ]
  ) -> Response:
    serializer = self.get_serializer(
      data = request.data
    )
    serializer.is_valid(
      raise_exception = True
    )
    user = serializer.save()
    return Response({
      'user': UserSerializer(
        user,
        context = self.get_serializer_context()
      ).data,
      'token': AuthToken.objects.create(user)[1]
    })
class LoginApi(GenericAPIView):
  serializer_class = LoginSerializer
  def post(
    self: 'RegisterApi',
    request: Request,
    *args: tuple,
    **kwargs: dict[
      str,
      object
    ]
  ) -> Response:
    serializer = self.get_serializer(
      data = request.data
    )
    serializer.is_valid(
      raise_exception = True
    )
    user = serializer.validated_data
    return Response({
      'user': UserSerializer(
        user,
        context = self.get_serializer_context()
      ).data,
      'token': AuthToken.objects.create(user)[1]
    })
class GetUserApi(RetrieveAPIView):
  permission_classes = [
    IsAuthenticated,
  ]
  serializer_class = UserSerializer
  def get_object(self: 'GetUserApi') -> UserSerializer:
    return self.request.user