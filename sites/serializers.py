from rest_framework_gis.serializers import GeoFeatureModelSerializer
from . models import Sites

# Serializer class to parse json
class SitesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Sites
        fields = '__all__'
        geo_field = 'location'