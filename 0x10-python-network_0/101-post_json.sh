#!/bin/bash
#GET request to the URL, and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" @"$2" "$1"
