import requests
import json
from influxdb import InfluxDBClient

client = InfluxDBClient(host="100.68.129.77", port=8086)
client.switch_database("covid")

URL = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=GEN,BEZ,death_rate,cases,deaths,cases_per_100k,cases_per_population,BL,last_update,cases7_per_100k,cases7_bl_per_100k,cases7_bl,death7_bl,cases7_lk,death7_lk&outSR=4326&f=json'
result = requests.get(URL)

output = json.loads(result.text)
refined = output['features']
data = [{k: v for k, v in d.items() if k == 'attributes'} for d in refined]
for d in data:
	json_body = [{
		"measurement": "GermanyData",
		"tags": {
			"State": d['attributes']["BL"],
			"city": d['attributes']["GEN"]},
		"fields":{
			"cases": d['attributes']["cases"],
			"cases7_bl":d['attributes']["cases7_bl"],
			"cases_per_100k":float(d['attributes']["cases_per_100k"]),
			"cases7_bl_per_100k":float(d['attributes']["cases7_bl_per_100k"]),
			"cases7_lk":d['attributes']["cases7_lk"],
			"cases_per_population":float(d['attributes']["cases_per_population"]),
			"deaths":d['attributes']["deaths"],
			"death7_bl":d['attributes']["death7_bl"],
			"death7_lk":d['attributes']["death7_lk"],
			"death_rate":float(d['attributes']["death_rate"]),
			# TODO parse time to understandable by grafana
			"last_update":d['attributes']["last_update"]
		}}]
	client.write_points(json_body)

print('done')
