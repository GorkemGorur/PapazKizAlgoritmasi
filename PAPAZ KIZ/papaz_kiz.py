import random as rnd
eslesme = []
turler = ["Karo","Kupa","Sinek","Maça"]
kizlar = [tur+" Kız" for tur in turler]
papazlar = [tur+" Papaz" for tur in turler]

kiztercihler   = {kiz : rnd.sample(papazlar,4) for kiz in kizlar} 
papaztercihler = {papaz : rnd.sample(kizlar,4) for papaz in papazlar}

while len(eslesme)<4:
	papaztalipler = {papaz : [] for papaz in papazlar}
	kiztalipler = {kiz : [] for kiz in kizlar}

	for kiz in kizlar:
		papaztalipler[kiztercihler[kiz][0]].append(kiz)
	eb = -1

	for papaz in papaztalipler:
		eski = eb
		eb = max(eb,len(papaztalipler[papaz]))
		if eski != eb:
			arananpapaz = papaz

	sirano = min([papaztercihler[arananpapaz].index(kiz) for kiz in papaztalipler[arananpapaz]])
	aranankiz = papaztercihler[arananpapaz][sirano]

	eslesme.append((arananpapaz,aranankiz))

	for kiz in papaztalipler[arananpapaz]:
		kiztercihler[kiz].pop(0)
	papazlar.remove(arananpapaz)
	kizlar.remove(aranankiz)
	for kiz in kiztercihler:
		try:
			kiztercihler[kiz].pop(kiztercihler[kiz].index(arananpapaz))
		except:
			pass
	for papaz in papaztercihler:
		try:
			papaztercihler[papaz].pop(papaztercihler[papaz].index(aranankiz))
		except:
			pass

	for papaz in papaztalipler:
		papaztalipler[papaz].clear()
	for kiz in kiztalipler:
		kiztalipler[kiz].clear()

print(eslesme)
