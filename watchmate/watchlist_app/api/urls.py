from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    StreamPlatformViewSet
)

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),
    ################################################################
    path('', include(router.urls)),
    # path("stream/", StreamPlatformListAV.as_view(), name="platform-list"),
    # path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name="platform-detail"),
    ################################################################
    # path("review/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    ################################################################
    path(
        "<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"
    ),  # Create
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list"),  # List
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
