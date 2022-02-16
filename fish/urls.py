from django.urls import path, include
from rest_framework import routers
from fish import views


app_name = 'fish'

router = routers.DefaultRouter()
router.register('add-view-fish', views.FishViewSet, basename='add_view_fish')

urlpatterns = [
    path('', include(router.urls)),
]