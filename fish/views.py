from rest_framework.response import Response
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from fish.serializers import *
from fish.models import *


# Create your views here.


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all().order_by('-timestamp')
    serializer_class = FishSerializer

