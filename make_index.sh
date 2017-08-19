curl -XPUT localhost:9200/$1/?pretty

curl -XPUT localhost:9200/$1/_settings?pretty -d '{
	"index": {
		"max_result_window": 1000000
	}
}'