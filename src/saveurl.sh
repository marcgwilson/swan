#! /bin/bash

host="http://0.0.0.0:8000"

set -e

url=$1

data='mutation {
  createUrl(url: "'"$url"'") {
    ok
    url {
      id
      url
      hashId
    }
  }
}'

data=$(curl -s \
  -X POST \
  -H "Content-Type: application/graphql" \
  --data "$data" \
  $host/graphql)

# echo $data
hashid=$(echo $data | jq -r '.data.createUrl.url.hashId')

echo "$host/$hashid"
