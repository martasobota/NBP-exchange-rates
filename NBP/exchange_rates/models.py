from django.db import models
from datetime import date

TABLES = (
	(1, 'A'),
	(2, 'B'),
	(3, 'C'),
	)

# CURRENCIES = 

class NBP(models.Model):
	table = models.IntegerField(choices=TABLES, blank=False, default=1)
	currency = models.CharField(max_length=64)
	code = models.CharField(max_length=4)
	effective_date = models.DateField(default=date.today)
	'''
	DecimalField jest bardziej odpowiedni dla operacji pieniężnych
	ze względu na większą precyzyjność w stosunku do FloatField
	'''
	mid = models.DecimalField(max_digits=16, decimal_places=12, default='0.0') 
	
#przeliczanie ze złotówek na walutę zeby móc pokaza inną parę walut