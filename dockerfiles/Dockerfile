FROM python:3.12-slim AS base-stage

ENV ENV=LOCAL
ARG APP_NAME=mediary

WORKDIR /home/${APP_NAME}

COPY ./requirements.txt .
COPY ./${APP_NAME} .
RUN pip install --no-cache-dir -r requirements.txt
RUN cat /etc/passwd


EXPOSE 8000
CMD [ "./scripts/entrypoint.sh" ]

