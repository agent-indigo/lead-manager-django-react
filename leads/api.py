from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import QuerySet
from .models import Lead
from .serializers import LeadSerializer
class LeadViewSet(ModelViewSet):
  serializer_class = LeadSerializer
  permission_classes = [
    IsAuthenticated,
  ]
  def get_queryset(self: 'LeadViewSet') -> QuerySet[Lead]:
    return Lead.objects.filter(
      user = self.request.user
    )
  def perform_create(
      self: 'LeadViewSet',
      serializer: LeadSerializer
    ) -> None:
    serializer.save(
      user = self.request.user
    )