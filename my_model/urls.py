from .views import MyModelItemViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', MyModelItemViewSet, basename='my-model')

urlpatterns = router.urls
