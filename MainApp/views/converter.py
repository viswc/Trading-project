from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import Candle
from pandas import *
import json
from django.conf import settings

def index(request):
	return render(request, "Index.html", {})

def list(request):
	reqCandles = Candle.objects.all()
	return render(request, "List.html", {
		"candles": reqCandles,
	})

def upload(request):
	if request.method == "POST":
		CSV = request.FILES.get('csvfile')
		reqNew = Candle.objects.create(csv = CSV)
		data = read_csv(str(str(settings.BASE_DIR) + reqNew.csv.url))

		ID = data['BANKNIFTY'].tolist()
		DATE = data['DATE'].tolist()
		TIME = data['TIME'].tolist()
		OPEN = data['OPEN'].tolist()
		HIGH = data['HIGH'].tolist()
		LOW = data['LOW'].tolist()
		CLOSE = data['CLOSE'].tolist()
		VOLUME = data['VOLUME'].tolist()

		reqNew.openl = OPEN[0]
		reqNew.time = TIME[0]
		reqNew.date = DATE[0]
		reqNew.high = max(HIGH)
		reqNew.close = CLOSE[-1]
		reqNew.volume = VOLUME[-1]
		reqNew.idL = ID[0]
		reqNew.save()

		json_dat = {"BANKNIFTY": reqNew.idl, "DATE": reqNew.date, "TIME": reqNew.time, "OPEN": reqNew.openl, "HIGH": reqNew.high, "CLOSE": reqNew.close, "VOLUME": reqNew.volume}
		json_object = json.dumps(json_dat, indent=4)
		with open(str("general/files/" + str(reqNew.idl) + str(reqNew.date) + str(reqNew.time) + ".json"), "w") as outfile:
			outfile.write(json_object)
		reqNew.json = str("general/files/" + str(reqNew.idl) + str(reqNew.date) + str(reqNew.time) + ".json")
		reqNew.save()
		return HttpResponseRedirect(reverse("Internship:list"))

	else:
		return render(request, "Upload.html", {})