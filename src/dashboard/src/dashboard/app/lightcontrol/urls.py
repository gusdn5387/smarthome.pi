from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ledstatus', views.LedStatusViewSet)
router.register(r'roomstatus', views.RoomStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
