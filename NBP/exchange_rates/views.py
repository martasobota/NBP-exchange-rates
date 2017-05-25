from django.shortcuts import render
from django.views import View
import json
import requests
from . import nbp_service
from django.views import generic

class NBPPage(generic.TemplateView):
    def get(self,request):
    	code = 'usd'
    	# nbp_data = nbp_service.get_data(code)
    	nbp_data = nbp_service
    	return render(request,'exchange_rates/nbp.html',nbp_data)