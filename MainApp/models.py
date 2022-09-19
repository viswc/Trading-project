from django.db import models
import uuid

class Candle(models.Model):
	dateCreated = models.DateTimeField(auto_now_add = True)
	dateModified = models.DateTimeField(auto_now = True)
	primaryKey = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
	csv = models.FileField(upload_to='general/files/')
	json = models.CharField(max_length = 32, default="CandleJSONServiceProvider")

	idl = models.CharField(max_length = 32, default="CandleIDServiceProvider")
	date = models.CharField(max_length = 32, default="CandleDateerviceProvider")
	time = models.CharField(max_length = 32, default="CandleTimeServiceProvider")
	openl = models.CharField(max_length = 32, default="CandleOpenServiceProvider")
	close = models.CharField(max_length = 32, default="CandleCloseServiceProvider")
	high = models.CharField(max_length = 32, default="CandleHighServiceProvider")
	volume = models.CharField(max_length = 32, default="CandleVolumeServiceProvider")