from rest_framework import generics

from women.models import Women
from women.serializers import WomenSerializer


class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
