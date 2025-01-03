from django.urls import path
from .views import ActionLogListCreateView, ActionLogRetrieveUpdateDestroyView

urlpatterns = [
    path('', ActionLogListCreateView.as_view(), name='actionlog-list-create'),
    path('<int:pk>/', ActionLogRetrieveUpdateDestroyView.as_view(), name='actionlog-detail'),
]