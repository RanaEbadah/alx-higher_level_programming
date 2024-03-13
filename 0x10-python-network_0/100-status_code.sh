#!/bin/bash
#GET request to the URL, and displays the body of the response.
curl -sX GET -o /dev/null -w "%{http_code}" "$1"
