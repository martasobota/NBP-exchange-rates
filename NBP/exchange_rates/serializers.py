from rest_framework import serializers
from exchange_rates.models import NBP, TABLES

# data = serializers.serialize("json", NBP.objects.all(), fields=('currency','code' 'mid'))

class NBPSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = NBP
		fields = ('table', 'currency', 'code', 'effective_date', 'rate')
