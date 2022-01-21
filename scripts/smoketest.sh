#!/bin/bash

FAILING=0

for p in olympus klima; do
  export PLAYGROUNDS_CONFIG=${p}.yaml
  echo $PLAYGROUNDS_CONFIG
  python index.py &
  DASH_PID=$!
  sleep 5
  RESP_CODE=$(curl --head --location --write-out %{http_code} --silent --output /dev/null http://127.0.0.1:8050/)
  echo $RESP_CODE
  kill `lsof -w -n -i tcp:8050 | awk '$2!="PID" {print $2;}'`
  if [ "$RESP_CODE" != "200" ];
  then
    echo "$p FAILED! ($RESP_CODE)"
    FAILING=1
  else
    echo "$p OK ($RESP_CODE)"
  fi
done

if [ $FAILING -eq 1 ];
then
  echo "ERROR"
  exit 1
else
  echo "SUCCESS"
  exit 0
fi
