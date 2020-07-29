from .models import LedStatus, RoomStatus
from rest_framework import serializers

class LedStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedStatus
        fields = '__all__'


class RoomStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = '__all__'

