from rest_framework import routers
from drf_user import views
# from user import views

router = routers.DefaultRouter()
router.register(r'user',views.UserViewset)





























# router.register(r'friends',myapp_views.FriendViewset)
# router.register(r'belongings',myapp_views.BelongingViewset)
# router.register(r'borrowings',myapp_views.BorrowedViewset)
# router.register(r'product',views.ProductViewset)
# router.register(r'cart',views.CartViewset)