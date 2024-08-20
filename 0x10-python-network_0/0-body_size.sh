#!/bin/bash
# sends a request to the provided url and displays the size of the response body in bytes
curl -sI "$1" | grep -i content-length | cut -d " " -f 2
