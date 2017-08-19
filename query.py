import sys, time
from elasticsearch import Elasticsearch
import json

def print_doc_src(doc):
	for field in doc["_source"]:
		print "%s: %s" % (field, doc["_source"][field])

if __name__ == "__main__":
	ES = Elasticsearch([{"host": "localhost", "port": 9200}])
	ES_INDEX = "people"
	ES_TYPE = "normals"

	match_all = {
		"query": {
			"match_all": {}
		}
	}

	exactly_gmail = {
		"query": {
			"term": {"domain": "gmail.com"}
		}
	}

	exactly_gmail_sorted_age = {
		"sort": [
				{"age": "asc"},
				{"balance": "desc"}
		],
		"query": {
			"term": {"domain": "gmail.com"}
		}
	}

	exactly_gmail_sorted_age_specific = {
		"sort": [
				{"age": "asc"},
				{"balance": "desc"}
		],
		"_source": [
			"name", "age", "balance"
		],
		"query": {
			"term": {"domain": "gmail.com"}
		}
	}

	all_tagline_grow_sticky = {
		"sort": [
				{"age": "asc"},
				{"balance": "desc"}
		],
		"_source": [
			"name", "age", "balance", "tagline"
		],
		"query": {
			"term": {"tagline": "sticky"}
		}	
	}

	idk = {
		"_source": [
			"name", "age", "balance", "tagline"
		],
		"query": {
			"bool": {
				"should": [
					{"match": {"tagline": "sticky"}},
					{"match": {"tagline": "grow"}}
				]
			}
		}	
	}

	count = ES.count(index="people")["count"]

	response = ES.search(index = ES_INDEX, size = 50, body = idk)

	result = response["hits"]["hits"]

	for doc in result:
		print_doc_src(doc)