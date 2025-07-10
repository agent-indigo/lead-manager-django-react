from django.db import models
from uuid import uuid4
# Create your models here.
class Lead(models.Model):
  class Meta:
    verbose_name = 'Lead'
    verbose_name_plural = f'{verbose_name}s'
    db_table = f'{verbose_name.lower()}s'
  id = models.UUIDField(
    primary_key = True,
    default = uuid4,
    editable = False
  )
  first_name = models.CharField()
  last_name = models.CharField()
  email_address = models.EmailField(
    unique = True
  )
  phone_number = models.CharField()
  message = models.TextField(
    blank = True
  )
  owner = models.ForeignKey(
    'auth.User',
    on_delete = models.CASCADE,
    related_name = 'leads',
    null = True
  )
  created_at = models.DateTimeField(
    auto_now_add = True
  )
  updated_at = models.DateTimeField(
    auto_now = True
  )