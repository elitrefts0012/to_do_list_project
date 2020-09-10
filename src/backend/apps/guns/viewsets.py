from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from guns.models import Gun
from guns.serializers import GunSerializer, ForSaleGunSerializer


class GunViewSet(viewsets.ModelViewSet):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list' and 'for_sale' not in self.request.query_params:
            return GunSerializer
        return ForSaleGunSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.action == 'list' and 'for_sale' not in self.request.query_params:
            qs = qs.filter(for_sale=True)
        return qs
