from django.urls import path
from .views import WishlistListCreateView, WishlistRetrieveUpdateDestroyView

urlpatterns = [
    path('', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('<int:pk>/', WishlistRetrieveUpdateDestroyView.as_view(), name='wishlist-detail'),
]
