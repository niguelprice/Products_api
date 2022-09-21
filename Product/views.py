from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product



@api_view(['GET'])
def Products_list(request):
    product = Product.objects.all()

    serializer = ProductSerializer(product, many=True)

    return Response(serializer.data)