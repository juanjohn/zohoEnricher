import re
import urllib
import urllib2

xml_response="<?xml version=\"1.0\" encoding=\"UTF-8\" ?><response uri=\"/crm/private/xml/Leads/getRecords\"><result><Leads><row no=\"1\"><FL val=\"LEADID\">1337722000000075040</FL><FL val=\"SMOWNERID\">1337722000000075001</FL><FL val=\"Lead Owner\"><![CDATA[Anoop Thomas Mathew]]></FL><FL val=\"Company\"><![CDATA[Profoundis]]></FL><FL val=\"First Name\"><![CDATA[Anoop]]></FL><FL val=\"Last Name\"><![CDATA[Thomas Mathew]]></FL><FL val=\"Email\"><![CDATA[]]>atmb4u@gmail.com</FL><FL val=\"No of Employees\"><![CDATA[0]]></FL><FL val=\"Annual Revenue\"><![CDATA[0]]></FL><FL val=\"SMCREATORID\">1337722000000075001</FL><FL val=\"Created By\"><![CDATA[Anoop Thomas Mathew]]></FL><FL val=\"MODIFIEDBY\">1337722000000075001</FL><FL val=\"Modified By\"><![CDATA[Anoop Thomas Mathew]]></FL><FL val=\"Created Time\"><![CDATA[2014-11-26 15:43:55]]></FL><FL val=\"Modified Time\"><![CDATA[2014-11-26 15:43:55]]></FL><FL val=\"Email Opt Out\"><![CDATA[false]]></FL><FL val=\"Salutation\"><![CDATA[Mr.]]></FL><FL val=\"Last Activity Time\"><![CDATA[2014-11-26 15:43:55]]></FL></row></Leads></result></response>"

regex_raw_id = re.compile(r'<FL val="LEADID">.{1,50}</FL>', re.I)
lead_raw_id_list=regex_raw_id.findall(xml_response)

regex_raw_email = re.compile(r'<FL val="Email">.{1,50}</FL>',re.I)
lead_raw_email_list=regex_raw_email.findall(xml_response)

x=0
for lead_id in lead_id_list:
	print lead_id
	regex = re.compile(r'\w+@\w+\.\w+', re.I)
	lead_email=regex.findall(lead_raw_email_list[x])
	if len(lead_email) is 1:
		print lead_email
	else:
		continue
	x=x+1