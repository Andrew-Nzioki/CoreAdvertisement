from django.urls import path
from . import views

urlpatterns = [
    path("api/advertisement/", views.ad_list),
    path("api/advertisement/<int:pk>/", views.ad_detail),

    path("api/adCampaigns/", views.adCampaign_list),
    path("api/adCampaigns/<int:pk>/", views.adCampaign_detail),

    path("api/adImpresssions/", views.adImpresssion_list),
    path("api/adImpresssions/<int:pk>/", views.adImpresssion_detail),

    
]