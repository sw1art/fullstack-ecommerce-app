from rest_framework import generics
from .models import ActionLog
from .serializers import ActionLogSerializer

class ActionLogListCreateView(generics.ListCreateAPIView):
    queryset = ActionLog.objects.all()
    serializer_class = ActionLogSerializer

class ActionLogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActionLog.objects.all()
    serializer_class = ActionLogSerializer