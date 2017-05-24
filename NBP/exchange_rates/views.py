from django.shortcuts import render
from django.views import View
import json
import requests
from . import nbp_service
from django.views import generic

# class NBPPage(generic.TemplateView):
#     def get(self,request):
#     	code = 'usd'
#     	# nbp_data = nbp_service.get_data(code)
#     	nbp_data = nbp_service
#     	return render(request,'exchange_rates/nbp.html',nbp_data)


class NBPPage(View):
    def get(self,request, NBP_code):
    	
    	rate = NBP.objects.get(pk=NBP_code)
    	ctx = { 'rate' : rate,

    	}
    	# nbp_data = nbp_service.get_data(code)
    	return render(request,'exchange_rates/nbp.html',nbp_data)