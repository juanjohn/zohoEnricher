#!/usr/bin/python

import urllib
import urllib2
import re

module_name = 'Leads'
authtoken = 'b2392a9cbe5999c67bf70e3619332b6f'
params = {'authtoken':authtoken,'scope':'crmapi','newFormat':'2'}
final_URL = "https://crm.zoho.com/crm/private/xml/"+module_name+"/getRecords"
data = urllib.urlencode(params)
request = urllib2.Request(final_URL,data)
response = urllib2.urlopen(request)
xml_response = response.read()

#regex = re.compile(r'\w+@\w+', re.I)

regex_raw_id = re.compile(r'<FL val="LEADID">.{1,50}</FL>', re.I)
raw_lead_id_list=regex_raw_id.findall(xml_response)

regex_raw_email = re.compile(r'<FL val="Email">.{1,50}</FL>',re.I)
raw_lead_email_list=regex_raw_email.findall(xml_response)

x=0
lead_id_list=[]
email_id_list=[]
for raw_lead_id in raw_lead_id_list:

	regex_id=re.compile(r'\d+', re.I)
	lead_id_list.append((regex_id.findall(raw_lead_id))[0])

	regex_email = re.compile(r'\w+@\w+\.\w+', re.I)
	email_id_list.append((regex_email.findall(raw_lead_email_list[x])))
	x=x+1

x=0

vibe_api_key="b9c2b1fe746feec13382fda8b4505acc"

for lead_id in lead_id_list:
	if len(email_id_list[x]) is 1:
		email_id=(email_id_list[x])[0]

		vibe_request_url="https://vibeapp.co/api/v1/initial_data/?api_key="+vibe_api_key+"&email="+email_id+".com"
    	vibe_response=urllib2.urlopen(vibe_request_url)
    	vibe_contact_json=vibe_response.read()
    	response.close()

	x=x+1

