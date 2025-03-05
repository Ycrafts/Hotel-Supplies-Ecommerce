from rest_framework.routers import SimpleRouter
from .views import (
    SupplierProfileViewSet,
    AddressViewSet, 
    BuyerProfileViewSet, 
    CustomUserViewSet
)

router = SimpleRouter()
router.register('supplier-profiles', SupplierProfileViewSet, basename='supplier-profile')
router.register('buyer-profiles', BuyerProfileViewSet, basename='buyer-profile')    
router.register('addresses', AddressViewSet, basename='address') 
router.register('users', CustomUserViewSet, basename='customuser')

urlpatterns = router.urls