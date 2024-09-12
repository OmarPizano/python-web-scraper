#!/bin/bash

#virtualenv venv

source ./venv/bin/activate

#pip instal -r requirements.txt

python ./scraper.py | jq

deactivate
