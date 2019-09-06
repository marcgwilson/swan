#! /bin/bash

host="http://0.0.0.0:8000"

set -e

hash=$1

data='query {
	getUrl: url(hashId: "'"$hash"'") {
  	url
  }
}'

data=$(curl -s \
  -X POST \
  -H "Content-Type: application/graphql" \
  --data "$data" \
  $host/graphql)


echo $data | jq -r '.data.getUrl.url'
