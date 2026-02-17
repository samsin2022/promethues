#!/bin/bash

# Ensure there is a space between 'while' and ':'
while :
do
    # Use curl to make the request, -s (silent) hides progress bars
    curl -s http://172.30.30.22:5001/ > /dev/null
    
    # Generate a random sleep time between 0 and 199 seconds
    SLEEP_TIME=$((RANDOM % 200))
    echo "Request sent. Sleeping for $SLEEP_TIME seconds..."
    sleep $SLEEP_TIME
done