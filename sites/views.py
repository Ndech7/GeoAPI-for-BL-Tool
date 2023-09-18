from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Sites
from . serializers import SitesSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def get_sites(request, format=None):
    # get all sites
    sites = Sites.objects.all()

    # serialize them
    serializer = SitesSerializer(sites, many=True)

    # return json
    return Response({'sites': serializer.data})
    

