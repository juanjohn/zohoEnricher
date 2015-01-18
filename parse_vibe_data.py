#!/usr/bin/python

import urllib
import urllib2
import re

vibe_api_key=""
lead="juanjhn@gmail.com"

vibe_request_url="https://vibeapp.co/api/v1/initial_data/?api_key="+vibe_api_key+"&email="+lead
vibe_response=urllib2.urlopen(vibe_request_url)
vibe_contact_json=vibe_response.read()

print vibe_contact_json

vibe_response.close()
