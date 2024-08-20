#!/bin/bash
# Displays all HTTP methods accepted by the server for the provided URL
curl -sI "$1" | grep -i "allow" | cut -d ' ' -f 2-
