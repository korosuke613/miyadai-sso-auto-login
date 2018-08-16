#! bash

echo "start login" >> ./log.txt
pipenv python miyadai_login.py >> ./log.txt
echo "end login" >> ./log.txt
