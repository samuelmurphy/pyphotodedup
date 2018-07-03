import boto3
import ConfigParser


def get_buckets():

#    client = 

# how to manage multiple autentication approaches to aws....
    
    s3 = boto3.resource('s3')
    
    bucket_list = client.list_buckets()




