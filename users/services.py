from django.db.models import QuerySet
from rest_framework.exceptions import NotFound

from .models import *
# , full_name: str, address: str,owner_type:OwnerType,flat:int,floor:int,people:int
class CarService:
    @classmethod
    def create(cls, phone:CustomUser):
        User.objects.create(phone=phone)
