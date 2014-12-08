#!/usr/bin/python

import urllib
import urllib2
import re

module_name = 'Leads'
authtoken = 'b2392a9cbe5999c67bf70e3619332b6f'
params = {'authtoken':authtoken,'scope':'crmapi'}
final_URL = "https://crm.zoho.com/crm/private/xml/"+module_name+"/getRecords"
data = urllib.urlencode(params)
request = urllib2.Request(final_URL,data)
response = urllib2.urlopen(request)
xml_response = response.read()

regex = re.compile(r'\w+@\w+', re.I)

leads_list=regex.findall(xml_response)

vibe_api_key="b9c2b1fe746feec13382fda8b4505acc"

for lead in leads_list:
    vibe_request_url="https://vibeapp.co/api/v1/initial_data/?api_key="+vibe_api_key+"&email="+lead+".com"
    vibe_response=urllib2.urlopen(vibe_request_url)
    vibe_contact_json=vibe_response.read()

    response.close()


