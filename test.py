# coding: utf-8

import boto3
from elasticsearch import Elasticsearch


def lambda_handler(event, context):
    pass
    print('test')
    es = Elasticsearch('search-cloudtrail-log-hjunjjhcomsxagtvy7chbmsyta.ap-northeast-1.es.amazonaws.com', port=80)
    print(es.search(index='cwl-2017.12.01'))








lambda_handler(1,1)



