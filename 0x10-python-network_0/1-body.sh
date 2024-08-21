#!/bin/bash
# Send a GET request to the URL and display only the body of the response if status code is 200

url=$1

# Send the GET request and store the HTTP status code and response body
response=$(curl -s -w "%{http_code}" -o /tmp/body.txt "$url")

# Extract the HTTP status code from the response
status_code="${response: -3}"

# Display the body if status code is 200
if [ "$status_code" -eq 200 ]; then
  cat /tmp/body.txt
fi
