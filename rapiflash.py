import urllib
import urllib2
import requests
import json
url = "http://api.devinmui.c9.io/api/v1"
def all():
  response = urllib2.urlopen(url + "/floods/")
  data = json.loads(response.read())
  return data
def find(id):
  response = urllib2.urlopen(url + "/floods/" + str(id))
  data = json.loads(response.read())
  return data
def create_data(current_level,normal_level,flooded,location,upstream):
  headers = {'content-type': 'application/json'}
  values = {'flood': {'current_level' : current_level, 'normal_level' : normal_level, 'flooded' : flooded, 'location' : location, 'upstream' : upstream}}
  values = json.dumps(values)
  d = requests.post(url + "/floods", data=values, headers=headers)
  return d.text
