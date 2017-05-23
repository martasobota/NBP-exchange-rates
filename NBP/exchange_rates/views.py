from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
import json
import requests
from . import nbp_service
from django.views import generic


# class USD_PLN_main(APIView):

# 	def get_object(self, pk):
# 	    try:
# 	    	return NBP.objects.get(pk=pk)
# 		except NBP.DoesNotExist:
# 		    raise Http404
# 	def get(self, request, id, format=None):
# 		nbp = self.get_object(id)
# 		serializer = NBPSerializer(nbp, context={"request": request}) 
# 		return Response(serializer.data)
# 	def delete(self, request, id, format=None):
# 		nbp = self.get_object(id)
# 		nbp.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
# 	def put(self, request, id, format=None): 
# 			nbp = self.get_object(id)
# 			serializer = NBPSerializer(nbp, data=request.data) 
# 			if serializer.is_valid():
# 				serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NBPPage(generic.TemplateView):
    def get(self,request):
        nbp_list = nbp_service.get_data('usd')
        return render(request,'nbp.html',nbp_list)