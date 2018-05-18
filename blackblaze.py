import sys
import base64
import json
import urllib2
import ConfigParser

print("---------------------------------")
Config = ConfigParser.ConfigParser()
Config
cfg = Config.read("config.txt")
Config.sections()

id = Config.get("blackblaze", "blackblaze_id")
bl_key = Config.get("blackblaze", "blackblaze_appkey")
id_and_key = id + ":" + bl_key

basic_auth_string = 'Basic ' + base64.b64encode(id_and_key)
headers = { 'Authorization': basic_auth_string }

act_auth_token = ""
api_url = ""

request = urllib2.Request(
    'https://api.backblazeb2.com/b2api/v1/b2_authorize_account',
    headers = headers
    )
response = urllib2.urlopen(request)
response_data = json.loads(response.read())

act_auth_token = response_data['authorizationToken']
api_url = response_data['apiUrl']

response.close()

print 'auth token:', response_data['authorizationToken']
print 'api url:', response_data['apiUrl']
print 'download url:', response_data['downloadUrl']
print 'minimum part size:', response_data['minimumPartSize']

# get buckets



request = urllib2.Request(
    '%s/b2api/v1/b2_list_buckets' % api_url,
    json.dumps({ 'accountId' : id }),
    headers = { 'Authorization': act_auth_token }
    )
response = urllib2.urlopen(request)
response_data = json.loads(response.read())
response.close()

#print json.dumps(response_data, indent=4)

for bucket in response_data["buckets"]:
    print bucket["bucketName"]
    bucket_id = bucket["bucketId"]

    request = urllib2.Request(
        '%s/b2api/v1/b2_list_file_names' % api_url,
        json.dumps({ 'bucketId' : bucket_id }),
        headers = { 'Authorization': act_auth_token }
        )

    response = urllib2.urlopen(request)
    response_data = json.loads(response.read())
    response.close()
    print response_data

