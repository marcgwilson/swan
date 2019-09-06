# URL Shortener
ID hashes are computed by first ciphering the object's ID using a 4-byte [Speck Cipher](https://pypi.org/project/simonspeckciphers/) then converted to a base62 left-padded 6 character string.

## Build Docker Image
```bash
make                    # build Docker image
docker-compose up -d    # run docker-compose file
./shell                 # bash shell of running container
``` 

## URLs
[Django Admin](http://0.0.0.0:8000/admin)  
[GraphQL](http://0.0.0.0:8000/graphql)  

## Django Admin
**username**: `root`  
**password**: `asdf1234`  

## shell scripts
`saveurl.sh` and `geturl.sh` use [`jq`](https://stedolan.github.io/jq/download/) for parsing **JSON** responses.  These can be run from inside the running Docker container.

```bash
./shell                                 # Connect to running docker container
./saveurl.sh https://www.google.ca      # Create shortened url
> http://0.0.0.0:8000/vXnrww
./geturl.sh https://www.google.ca       # Query shortened url
> http://0.0.0.0:8000/vXnrww
```

## GraphQL Queries
```graphql
query {
  allUrls {
    id
    url
  }
}

query {
  url(id: 1) {
    hashId
  }
  anotherUrl: url(url: "https://www.google.com") {
    url
    hashId
  }
}

mutation {
  createUrl(url: "https://www.theverge.com") {
    ok
    url {
      id
      url
      hashId
    }
  }
}
```

## Developement
```bash
docker-compose -f docker-compose-dev.yml up -d    # Start container with src directory mounted to /root/src
./shell                                           # Get bash shell in container
./bootstrap.sh                                    # Create database
./manage.py test                                  # Run tests
./manage.py shell_plus                            # Get Django shell
```
