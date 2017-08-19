# <argv1> num of records to generate

from faker import Factory
import sys, time
from elasticsearch import Elasticsearch
import random

class Person:

	def __init__(self):
		self.personal_info = {}
		self.personal_info["name"] = FAKE.name()
		self.personal_info["address"] = FAKE.street_address()
		self.personal_info["state"] = FAKE.state()
		self.personal_info["lorem"] = FAKE.text(max_nb_chars=100, ext_word_list=None)
		self.personal_info["color"] = FAKE.safe_color_name()
		self.personal_info["tagline"] = FAKE.bs()
		self.personal_info["domain"] = FAKE.free_email_domain()
		self.personal_info["balance"] = float("%.2f" % random.uniform(100000, 1000000))
		self.personal_info["age"] = random.randint(18, 100)

def gen_people(n):
	print "Starting to generate %s people." % n
	start = time.time()
	people = []

	for i in range(SIZE):
		if i % 1000 == 0:
			print "Generating person %s." % (i + 1)
		new_person = Person()
		people.append(new_person)

	end = time.time()
	print "Generation of %s people done. Took %ss." % (n, str(end - start))
	return people

def build_bulk(people):
	count = ES.count(index="people")["count"]
	doc_id = count + 1

	bulk_data = []

	for person in people:
		op_dict = {
			"index": {
				"_index": ES_INDEX,
				"_type": ES_TYPE,
				"_id" : doc_id
			}
		}
		bulk_data.append(op_dict)
		bulk_data.append(person.personal_info)
		doc_id = doc_id + 1

	return bulk_data

def post_bulk(data):
	print "Starting to upsert %s people." % SIZE
	start = time.time()
	response = ES.bulk(index = ES_INDEX, body = bulk_data, refresh = True)
	end = time.time()
	print "Upserting %s people done. Took %ss." % (SIZE, str(end - start))

if __name__ == "__main__":
	SIZE = int(sys.argv[1])
	FAKE = Factory.create()
	ES = Elasticsearch([{"host": "localhost", "port": 9200}])
	ES_INDEX = "people"
	ES_TYPE = "normals"

	people = gen_people(SIZE)

	bulk_data = build_bulk(people)

	post_bulk(bulk_data)
	#response = ES.count(index="people")


