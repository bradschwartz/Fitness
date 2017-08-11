#!/bin/bash
if [ $# -ne 1 ]
then
    echo "Name of image  needs to be provided."
    echo "Usage: ./ecr.sh <name_of_image>"
    exit 1
fi
`aws ecr get-login --no-include-email --region us-west-2`
docker build -t $1 .

docker tag $1:latest 896031365602.dkr.ecr.us-west-2.amazonaws.com/$1:latest
docker push 896031365602.dkr.ecr.us-west-2.amazonaws.com/$1:latest