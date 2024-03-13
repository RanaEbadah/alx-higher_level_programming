#!/bin/bash
#GET request to the URL, and displays the body of the response.
curl -sX GET "0.0.0.0:5000/catch_me" -d "You got me!"