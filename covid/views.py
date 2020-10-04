from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json
	api_request = requests.get("https://api.covid19api.com/summary")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {"api": api})

def india(request):
	import requests
	import json
	nation_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	nation = json.loads(nation_request.content)
	return render(request, 'india.html', {"nation": nation})

def states(request):
    return render(request, 'states.html', {})

def westbengal(request):
	import requests
	import json
	wb_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	wb = json.loads(wb_request.content)
	return render(request, 'westbengal.html', {"wb": wb})

def maharashtra(request):
	import requests
	import json
	mh_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	mh = json.loads(mh_request.content)
	return render(request, 'maharashtra.html', {"mh": mh})

def andhrapradesh(request):
	import requests
	import json
	ap_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ap = json.loads(ap_request.content)
	return render(request, 'andhrapradesh.html', {"ap": ap})

def karnataka(request):
	import requests
	import json
	ka_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ka = json.loads(ka_request.content)
	return render(request, 'karnataka.html', {"ka": ka})

def tamilnadu(request):
	import requests
	import json
	tn_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	tn = json.loads(tn_request.content)
	return render(request, 'tamilnadu.html', {"tn": tn})

def uttarpradesh(request):
	import requests
	import json
	up_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	up = json.loads(up_request.content)
	return render(request, 'uttarpradesh.html', {"up": up})

def delhi(request):
	import requests
	import json
	dl_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	dl = json.loads(dl_request.content)
	return render(request, 'delhi.html', {"dl": dl})

def odisha(request):
	import requests
	import json
	od_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	od = json.loads(od_request.content)
	return render(request, 'odisha.html', {"od": od})

def kerala(request):
	import requests
	import json
	kl_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	kl = json.loads(kl_request.content)
	return render(request, 'kerala.html', {"kl": kl})

def telangana(request):
	import requests
	import json
	tg_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	tg = json.loads(tg_request.content)
	return render(request, 'telangana.html', {"tg": tg})

def bihar(request):
	import requests
	import json
	br_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	br = json.loads(br_request.content)
	return render(request, 'bihar.html', {"br": br})

def assam(request):
	import requests
	import json
	ass_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ass = json.loads(ass_request.content)
	return render(request, 'assam.html', {"ass": ass})

def rajasthan(request):
	import requests
	import json
	rj_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	rj = json.loads(rj_request.content)
	return render(request, 'rajasthan.html', {"rj": rj})

def gujarat(request):
	import requests
	import json
	gj_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	gj = json.loads(gj_request.content)
	return render(request, 'gujarat.html', {"gj": gj})

def madhyapradesh(request):
	import requests
	import json
	mp_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	mp = json.loads(mp_request.content)
	return render(request, 'madhyapradesh.html', {"mp": mp})

def haryana(request):
	import requests
	import json
	hr_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	hr = json.loads(hr_request.content)
	return render(request, 'haryana.html', {"hr": hr})

def chhattisgarh(request):
	import requests
	import json
	ct_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ct = json.loads(ct_request.content)
	return render(request, 'chhattisgarh.html', {"ct": ct})

def punjab(request):
	import requests
	import json
	pb_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	pb = json.loads(pb_request.content)
	return render(request, 'punjab.html', {"pb": pb})

def jharkhand(request):
	import requests
	import json
	jh_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	jh = json.loads(jh_request.content)
	return render(request, 'jharkhand.html', {"jh": jh})

def jammuandkashmir(request):
	import requests
	import json
	jk_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	jk = json.loads(jk_request.content)
	return render(request, 'jammuandkashmir.html', {"jk": jk})

def uttarakhand(request):
	import requests
	import json
	ut_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ut = json.loads(ut_request.content)
	return render(request, 'uttarakhand.html', {"ut": ut})

def goa(request):
	import requests
	import json
	ga_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ga = json.loads(ga_request.content)
	return render(request, 'goa.html', {"ga": ga})

def puducherry(request):
	import requests
	import json
	py_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	py = json.loads(py_request.content)
	return render(request, 'puducherry.html', {"py": py})

def tripura(request):
	import requests
	import json
	tr_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	tr = json.loads(tr_request.content)
	return render(request, 'tripura.html', {"tr": tr})

def himachalpradesh(request):
	import requests
	import json
	hp_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	hp = json.loads(hp_request.content)
	return render(request, 'himachalpradesh.html', {"hp": hp})

def chandigarh(request):
	import requests
	import json
	ch_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ch = json.loads(ch_request.content)
	return render(request, 'chandigarh.html', {"ch": ch})

def manipur(request):
	import requests
	import json
	mn_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	mn = json.loads(mn_request.content)
	return render(request, 'manipur.html', {"mn": mn})

def arunachalpradesh(request):
	import requests
	import json
	ar_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ar = json.loads(ar_request.content)
	return render(request, 'arunachalpradesh.html', {"ar": ar})

def meghalaya(request):
	import requests
	import json
	ml_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ml = json.loads(ml_request.content)
	return render(request, 'meghalaya.html', {"ml": ml})

def nagaland(request):
	import requests
	import json
	nl_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	nl = json.loads(nl_request.content)
	return render(request, 'nagaland.html', {"nl": nl})

def ladakh(request):
	import requests
	import json
	lk_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	lk = json.loads(lk_request.content)
	return render(request, 'ladakh.html', {"lk": lk})

def andamanandnicobarislands(request):
	import requests
	import json
	an_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	an = json.loads(an_request.content)
	return render(request, 'andamanandnicobarislands.html', {"an": an})

def sikkim(request):
	import requests
	import json
	sk_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	sk = json.loads(sk_request.content)
	return render(request, 'sikkim.html', {"sk": sk})

def mizoram(request):
	import requests
	import json
	mz_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	mz = json.loads(mz_request.content)
	return render(request, 'mizoram.html', {"mz": mz})

def damananddiudadraandnagarhaveli(request):
	import requests
	import json
	dn_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	dn = json.loads(dn_request.content)
	return render(request, 'damananddiudadraandnagarhaveli.html', {"dn": dn})

def lakshadweep(request):
	import requests
	import json
	ld_request = requests.get("https://api.covidindiatracker.com/state_data.json")
	ld = json.loads(ld_request.content)
	return render(request, 'lakshadweep.html', {"ld": ld})