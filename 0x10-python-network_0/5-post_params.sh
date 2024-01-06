#!/bin/bash
#GET request to the URL, and displays the body of the response.
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
