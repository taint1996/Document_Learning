from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

es.indices.create(index='test-index', ignore=400)

####### Timeout
# only wait for 1 second, regardless of the client's default
print("Timeout: ", es.cluster.health(wait_for_status="yellow", request_timeout=1))

###### Response Filtering
print("Response: ", es.search(index="test-index", filter_path=['hits.hits._id', 'hits.hits._type']))


# doc = {
#   'author': "BeokaKun",
#   'text': 'ElasticSearch: cool, bonsai cool.',
#   'timestamp': datetime.now(),
# }

# res1 = es.index(index="test-index", doc_type = "tweet", id= 1, body=doc)
# print(res1['result'])

# res2 = es.get(index="test-index", doc_type= "tweet", id=1)
# print("Get res: ", res2)
# print("Res2: ", res2['_source'])

# res3 = es.indices.refresh(index="test-index")
# print(res3)

# res4 = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Res4: ", res4)
# print("Got %d Hits: " % res4['hits']['total'])

# for hit in res4['hits']['hits']:
#   print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
