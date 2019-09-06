#! /bin/bash

host="http://0.0.0.0:8000"

set -e

url=$1

data='query {
	url(url: "'"$url"'") {
  	hashId
  }
}'

data=$(curl -s \
  -X POST \
  -H "Content-Type: application/graphql" \
  --data "$data" \
  $host/graphql)

hashid=$(echo $data | jq -r '.data.url.hashId')

echo "$host/$hashid"