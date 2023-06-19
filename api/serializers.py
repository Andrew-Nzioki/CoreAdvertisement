from rest_framework.serializers import ModelSerializer
from .models import *


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class AdCampaignSerializer(ModelSerializer):
    class Meta:
        model = AdCampaigns
        fields = '__all__'


class AdImpresssionSerializer(ModelSerializer):
    class Meta:
        model = AdImpresssions
        fields = '__all__'

