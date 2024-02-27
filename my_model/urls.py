from .views import MyModelSerializer


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', MyModelSerializer, basename='my-model')

urlpatterns = router.urls
