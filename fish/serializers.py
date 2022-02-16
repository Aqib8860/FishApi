from rest_framework import serializers
from fish import models


class FishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fish
        fields = '__all__'
