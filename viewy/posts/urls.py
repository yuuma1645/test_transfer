from django.urls import path
from .views import (
 MangaCreateView, VisitorPostListView, PostListView, VideoCreateView, StarView, FavoriteView, RecommendPostView, GetRecommendUsers, FavoritePostListView, PosterPageView, HashtagPostListView, HashtagDimensionChangeView, HashtagPageView, FollowListView, FollowPageView, GetMoreFollowView, GetMorePreviousFollowView, GetMorePreviousCollectionView, DeleteCollectionView, RenameCollectionView, PosterPostListView, MyAccountView, SettingView, PinPostView, DeletePostView, AddPostView, SearchPageView, HotHashtagView, FavoritePageView, CollectionsMenuView, CollectionPageView, CollectionPostListView, GetMoreCollectionView, CreateNewCollection, BePartnerPageView, SubmitReportView, MyPostView, HiddenPostView, UnpublishedPostView, UpdateScheduledTimeView, AutoCorrectView, GetMorePostsView, GetMoreFavoriteView, GetMorePreviousFavoriteView, GetMorePosterPostsView, GetMorePreviousPosterPostsView, GetMoreHashtagView, GetMorePreviousHashtagView, AdsViewCount, WideAdsViewCount, AdsClickCount, WideAdsClickCount, AddToCollectionView, RemoveFromCollectionView, CreateCollectionAndAddPost, CollectionsForPostView, MyFollowListView, MyBlockListView, FreezeNotificationRequest, FreezeNotificationRequestSuccessView, FreezeListView, EmoteCountView, ViewDurationCountView, ShowMessageView, TestStreamingView, HandleEventParticipationView
)

app_name = 'posts'

urlpatterns = [
   path('manga_create/', MangaCreateView.as_view(), name='manga_create'),
   path('video_create/', VideoCreateView.as_view(), name='video_create'),
   path('postlist/', PostListView.as_view(), name='postlist'),
   path('visitor_postlist/', VisitorPostListView.as_view(), name='visitor_postlist'),
   path('get_more_posts/', GetMorePostsView.as_view(), name='get_more_posts'),
   path('star/', StarView.as_view(), name='star'),
   path('favorite/<int:pk>/', FavoriteView.as_view(), name='favorite'),
   path('recommend/', RecommendPostView.as_view(), name='recommend'),
   path('get_recommend_users/<int:post_id>/', GetRecommendUsers.as_view(), name='get_recommend_users'),
   path('fovorite_page/', FavoritePageView.as_view(), name='favorite_page'),
   path('fovorite_list/', FavoritePostListView.as_view(), name='favorite_list'),
   path('get_more_favorite/',  GetMoreFavoriteView.as_view(), name='get_more_favorite'),
   path('get_more_previous_favorite/',  GetMorePreviousFavoriteView.as_view(), name='get_more_previous_favorite'),
   path('collections_menu/', CollectionsMenuView.as_view(), name='collections_menu'),
   path('collection_page/<int:collection_id>/', CollectionPageView.as_view(), name='collection_page'),
   path('collection_list/<int:collection_id>/', CollectionPostListView.as_view(), name='collection_list'),
   path('get_more_collection/', GetMoreCollectionView.as_view(), name='get_more_collection'),
   path('get_more_previous_collection/', GetMorePreviousCollectionView.as_view(), name='get_more_previous_collection'),
   path('delete_collection/<int:collection_id>/', DeleteCollectionView.as_view(), name='delete_collection'),
   path('rename_collection/<int:collection_id>/', RenameCollectionView.as_view(), name='rename_collection'),
   path('create_new_collection/', CreateNewCollection.as_view(), name='create_new_collection'),
   path('hashtag_dimension_change/', HashtagDimensionChangeView.as_view(), name='hashtag_dimension_change'),
   path('hashtag/<str:hashtag>/', HashtagPageView.as_view(), name='hashtag'),
   path('hashtag_list/<str:hashtag>/', HashtagPostListView.as_view(), name='hashtag_list'),
   path('get_more_hashtag/', GetMoreHashtagView.as_view(), name='get_more_hashtag'),
   path('get_more_previous_hashtag/', GetMorePreviousHashtagView.as_view(), name='get_more_previous_hashtag'),
   path('posts/follow_list/', FollowListView.as_view(), name='follow_list'),
   path('follow_page/', FollowPageView.as_view(), name='follow_page'),
   path('get_more_follow/',  GetMoreFollowView.as_view(), name='get_more_follow'),
   path('get_more_previous_follow/',  GetMorePreviousFollowView.as_view(), name='get_more_previous_follow'),
   # path('back/', BackView.as_view(), name='back'),
   path('poster_page/<str:username>/', PosterPageView.as_view(), name='poster_page'),
   path('poster_post_list/<str:username>/', PosterPostListView.as_view(), name='poster_post_list'),
   path('get_more_poster_posts/',  GetMorePosterPostsView.as_view(), name='get_more_poster_posts'),
   path('get_more_previous_poster_posts/',  GetMorePreviousPosterPostsView.as_view(), name='get_more_previous_poster_posts'), 
   path('add_post/', AddPostView.as_view(), name='add_post'),
   path('my_account/', MyAccountView.as_view(), name='my_account'),   
   path('my_posts/', MyPostView.as_view(), name='my_posts'), 
   path('hidden_post/', HiddenPostView.as_view(), name='hidden_post'), 
   path('unpublished_post/', UnpublishedPostView.as_view(), name='unpublished_post'), 
   path('update_scheduled_time/', UpdateScheduledTimeView.as_view(), name='update_scheduled_time'),
   path('my_follow_list/', MyFollowListView.as_view(), name='my_follow_list'),
   path('block-list/', MyBlockListView.as_view(), name='block_list'),
   path('freeze_notification_request/', FreezeNotificationRequest.as_view(), name='freeze_notification_request'),
   path('freeze_notification_request_success/', FreezeNotificationRequestSuccessView.as_view(), name='freeze_notification_request_success'),
   path('freeze-list/', FreezeListView.as_view(), name='freeze_list'),
   path('pin_post/', PinPostView.as_view(), name='pin_post'),
   path('delete_post/', DeletePostView.as_view(), name='delete_post'),
   path('setting/', SettingView.as_view(), name='setting'),   
   path('searchpage/', SearchPageView.as_view(), name='searchpage'),
   path('hothashtag/', HotHashtagView.as_view(), name='hothashtag'),
   path('auto_correct/', AutoCorrectView.as_view(), name='auto_correct'),
   path('be_partner/', BePartnerPageView.as_view(), name='be_partner'),
   path('ads_view_count/<int:ad_id>', AdsViewCount.as_view(), name='ads_view_count'),
   path('wideads_view_count/<int:ad_id>', WideAdsViewCount.as_view(), name='wideads_view_count'),
   path('ads_click_count/<int:ad_id>', AdsClickCount.as_view(), name='ads_click_count'),
   path('wideads_click_count/<int:ad_id>', WideAdsClickCount.as_view(), name='Wideads_click_count'),
   path('add_to_collection/', AddToCollectionView.as_view(), name='add_to_collection'),
   path('remove_from_collection/', RemoveFromCollectionView.as_view(), name='remove_from_collection'),
   path('create_collection_and_add_post/', CreateCollectionAndAddPost.as_view(), name='create_collection_and_add_post'),
   path('get_collections_for_post/<int:post_id>/', CollectionsForPostView.as_view(), name='get_collections_for_post'),
   path('report/', SubmitReportView.as_view(), name='report'),
   path('emote_count/<int:post_id>/<int:emote_number>/', EmoteCountView.as_view(), name='emote_count'),
   path('view_duration_count/', ViewDurationCountView.as_view(), name='view_duration_count'),
   path('show_message/', ShowMessageView.as_view(), name='show_message'),
   path('test_streaming/', TestStreamingView.as_view(), name='test_streaming'),
   path('handle_event_participation/', HandleEventParticipationView.as_view(), name='handle_event_participation'),
]
