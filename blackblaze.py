import sys
import base64
import json
import urllib2

#id_and_key = 'hexAccountId_value:accountKey_value'
id_and_key = 'e998c5598bb5:001941f0ac13642fa524fd8b9a2041e3ed3c605955'

basic_auth_string = 'Basic ' + base64.b64encode(id_and_key)
headers = { 'Authorization': basic_auth_string }

act_auth_token = ""

request = urllib2.Request(
    'https://api.backblazeb2.com/b2api/v1/b2_authorize_account',
    headers = headers
    )
response = urllib2.urlopen(request)
response_data = json.loads(response.read())

act_auth_token = response_data['authorizationToken']

response.close()

print 'auth token:', response_data['authorizationToken']
print 'api url:', response_data['apiUrl']
print 'download url:', response_data['downloadUrl']
print 'minimum part size:', response_data['minimumPartSize']

# get buckets


request = urllib2.Request(
    '%s/b2api/v1/b2_list_buckets' % api_url,
    json.dumps({ 'accountId' : account_id }),
    headers = { 'Authorization': act_auth_token }
    )
response = urllib2.urlopen(request)
response_data = json.loads(response.read())
response.close()
