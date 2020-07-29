from rest_framework import viewsets

from .models import LedStatus, RoomStatus
from .serializers import LedStatusSerializer, RoomStatusSerializer

class LedStatusViewSet(viewsets.ModelViewSet):
    queryset = LedStatus.objects.all().order_by('-created_at')
    serializer_class = LedStatusSerializer

class RoomStatusViewSet(viewsets.ModelViewSet):
    queryset = RoomStatus.objects.all().order_by('-created_at')
    serializer_class = RoomStatusSerializer


# Create your views here.

