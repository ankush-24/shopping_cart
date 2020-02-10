from rest_framework import routers
from rental import api_views as myapp_views
from user import views

router = routers.DefaultRouter()
router.register(r'friends',myapp_views.FriendViewset)
router.register(r'belongings',myapp_views.BelongingViewset)
router.register(r'borrowings',myapp_views.BorrowedViewset)
router.register(r'product',views.ProductViewset)
router.register(r'cart',views.CartViewset)
