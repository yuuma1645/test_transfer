from django.urls import path
from .views import (
  AdCampaignsListView, AdCampaignDetailView, CampaignFormView, AdMangaCreateView, AdVideoCreateView, IsHiddenToggle, AdViewButton, EditAdCampaignView, AdCampaignStatusView, AdInfoDelete, AdCampaignDelete, UpdateAdClickCountView
)
from . import views

app_name = 'advertisement'

urlpatterns = [ 
  path('ad_campaigns_list/', AdCampaignsListView.as_view(), name='ad_campaigns_list'),
  path('ad_campaign_detail/<int:campaign_id>/', AdCampaignDetailView.as_view(), name='ad_campaign_detail'),
  path('campaign_form/', CampaignFormView.as_view(), name='campaign_form'),
  path('ad_manga_create/', AdMangaCreateView.as_view(), name='ad_manga_create'),
  path('ad_video_create/', AdVideoCreateView.as_view(), name='ad_video_create'),
  path('is_hidden_toggle/', IsHiddenToggle.as_view(), name='is_hidden_toggle'),
  path('ad_view_button/<int:post_id>/', AdViewButton.as_view(), name='ad_view_button'),
  path('edit_ad_campaign/<int:campaign_id>/', EditAdCampaignView.as_view(), name='edit_ad_campaign'),
  path('ad_campaign_status/<int:campaign_id>/', AdCampaignStatusView.as_view(), name='ad_campaign_status'),
  path('delete_ad_info/<int:ad_info_id>/', AdInfoDelete.as_view(), name='delete_ad_info'),
  path('delete_ad_campaign/<int:campaign_id>/', AdCampaignDelete.as_view(), name='delete_ad_campaign'),
  path('update_ad_click_count/<int:post_id>/', UpdateAdClickCountView.as_view(), name='update_ad_click_count'),
]