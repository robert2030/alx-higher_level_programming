#!/bin/bash
# Sends a GET request to the provided URL and displays the body of the response (only for 200 status code)
curl -sX GET $1 -L
