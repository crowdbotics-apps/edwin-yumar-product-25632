from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    VendorViewSet,
    LocationViewSet,
    FavoritesViewSet,
    VendorDetailViewSet,
    CategoryViewSet,
    FaqViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    MyScheduleViewSet,
    SponsorViewSet,
)

router = DefaultRouter()
router.register("myschedule", MyScheduleViewSet)
router.register("presenter", PresenterViewSet)
router.register("vendordetail", VendorDetailViewSet)
router.register("sponsor", SponsorViewSet)
router.register("faq", FaqViewSet)
router.register("location", LocationViewSet)
router.register("vendor", VendorViewSet)
router.register("category", CategoryViewSet)
router.register("schedule", ScheduleViewSet)
router.register("favorites", FavoritesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
