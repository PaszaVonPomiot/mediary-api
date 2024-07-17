#!/usr/bin/env bash

APP_DIR="app"
APP_HOST="0.0.0.0"
APP_PORT=8000

echo "Starting FastAPI..."
echo "Environment: $APP_ENV"

if [ "$APP_ENV" == "LOCAL" ]; then
  exec uvicorn main:app --app-dir $APP_DIR \
                        --host $APP_HOST \
                        --port $APP_PORT \
                        --reload
else
  exec uvicorn main:app --app-dir $APP_DIR \
                        --host $APP_HOST \
                        --port $APP_PORT \
                        --header server:HIDDEN;
fi
