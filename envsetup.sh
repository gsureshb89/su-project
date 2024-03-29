#!/bin/bash

if [ -d "env" ]
then
	echo "python virtual env exists"
else
	python3 -m venv env
fi

echo $PWD
source env/bin/activate

pip install -r requirement.txt

if [ -d "logs" ]
then
	echo "Log folder exists"
else
	mkdir logs
	touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs

echo "envsetup finished"

