FROM python:3.12-slim AS base-stage

ARG APP_NAME=mediary
ENV ENV=LOCAL

WORKDIR /home/${APP_NAME}

COPY ./requirements.txt .
COPY ./${APP_NAME} .

RUN apt-get update && apt-get install -y procps \
	&& rm -rf /var/lib/apt/lists/* \
	&& pip install --no-cache-dir -r requirements.txt \
	&& adduser --disabled-password --gecos "" --home "/home/${APP_NAME}" --shell /usr/sbin/nologin ${APP_NAME} \
	&& chown -R ${APP_NAME}:${APP_NAME} /home/${APP_NAME}

EXPOSE 8000

USER ${APP_NAME}
CMD [ "./scripts/entrypoint.sh" ]
