#!/bin/bash

export DISPLAY=:0

pipenv run python ./miyadai_login.py >>./cron_log.txt 2>>./error-log.txt

