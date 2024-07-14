#!/bin/bash

echo "Environment: $ENV"
echo "Launching FastAPI"

if [ "$ENV" == "LOCAL" ]; then
  exec uvicorn main:app --app-dir app/ \
                        --host 0.0.0.0 \
                        --port 8000 \
                        --reload
else
  exec uvicorn main:app --app-dir app/ \
                        --host 0.0.0.0 \
                        --port 8000 \
                        --header server:HIDDEN;
fi
