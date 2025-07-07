#!bin/bash

# This script reads and prints environment variables from printenv command
# It is intended to be used in a Docker container
for (( ; ; ))
do
    echo "Reading environment variables..."
    printenv
    echo -e "\n Sleeping for 2 seconds...\n"
    #print the date 
    date
    sleep 2
done