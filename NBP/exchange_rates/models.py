from django.db import models

TABLES = (
	(1, 'A'),
	(2, 'B'),
	(3, 'C'),
	)

# CURRENCIES = 

class NBP(models.Model):
	table = models.IntegerField(choices=TABLES)
	currency = models.CharField(max_length=64)
	code = models.CharField(max_length=4)
	effective_date = models.DateField()
	rate = models.FloatField(max_length=8)

# class Exchange_rates(models.Model):
# 	from_rate = models.
# 	to_rate = models.
	
