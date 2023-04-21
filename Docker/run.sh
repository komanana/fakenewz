#!/usr/bin/bash
nohup python3 /home/CS06-1/backend/manage.py runserver 0.0.0.0:8000 >> /home/CS06-1/run.log 2>&1 &
service nginx restart
tail -f /home/CS06-1/run.log