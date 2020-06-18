from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.additional_data.models import Village, Destination,  Parcel, TreeSpecie, OvenType
from apps.additional_data.serializers import (
    VillageSerializer, DestinationSerializer, ParcelSerializer, TreeSpecieSerializer, OvenTypeSerializer
)
from config.swagger_schema import CustomSchema


class AdditionalDataViewSet(ViewSet):
    """
    Viewset with additional data
    """
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    schema = CustomSchema()

    @action(methods=['get'], detail=False, filter_backends=(SearchFilter,), search_fields=('name',))
    def all_data(self, request):
        data = {
            'villages': VillageSerializer(Village.objects.all(), many=True).data,
            'parcels': ParcelSerializer(Parcel.objects.all(), many=True).data,
            'destinations': DestinationSerializer(Destination.objects.all(), many=True).data,
            'tree_species': TreeSpecieSerializer(TreeSpecie.objects.all(), many=True).data,
            'oven_types': OvenTypeSerializer(OvenType.objects.all(), many=True).data,
        }
        return Response(data)


class ParcelViewSet(ModelViewSet):
    schema = CustomSchema()
    filter_backends = (SearchFilter,)
    serializer_class = ParcelSerializer
    queryset = Parcel.objects.all()


class VillageViewSet(ModelViewSet):
    schema = CustomSchema()
    filter_backends = (SearchFilter,)
    serializer_class = VillageSerializer
    queryset = Village.objects.all()


class DestinationViewSet(ModelViewSet):
    schema = CustomSchema()
    filter_backends = (SearchFilter,)
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()


class TreeSpecieViewSet(ModelViewSet):
    schema = CustomSchema()
    filter_backends = (SearchFilter,)
    serializer_class = TreeSpecieSerializer
    queryset = TreeSpecie.objects.all()


class OvenTypeViewSet(ModelViewSet):
    schema = CustomSchema()
    filter_backends = (SearchFilter,)
    serializer_class = OvenTypeSerializer
    queryset = OvenType.objects.all()