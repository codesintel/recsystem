from rest_framework import serializers
from .models import RecommendedItems


class RecommendedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecommendedItems
        fields="__all__"