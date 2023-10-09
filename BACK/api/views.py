from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)