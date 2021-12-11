#!/bin/sh

python producer.py &
echo 'producer running'
sleep 60
echo 'after sleeping'
python consumer.py &
