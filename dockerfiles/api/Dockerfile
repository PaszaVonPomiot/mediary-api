ARG APP_NAME=mediary

# ------------------------------------------------------------------------------

FROM python:3.12-slim AS base

ARG APP_NAME
ENV PATH=/home/${APP_NAME}/.venv/bin:$PATH

# ------------------------------------------------------------------------------

FROM base AS builder

WORKDIR /home/${APP_NAME}
COPY ${APP_NAME} ./requirements.txt ./
RUN pip install uv && \
    uv venv /home/${APP_NAME}/.venv && \
    uv pip install -r requirements.txt

# ------------------------------------------------------------------------------

FROM base AS runner

RUN find /etc/skel -type f -name ".*" -delete \
    && adduser --disabled-password --comment "Application User" \
    --home "/home/${APP_NAME}" --shell /usr/sbin/nologin ${APP_NAME}
WORKDIR /home/${APP_NAME}
COPY --chown=${APP_NAME}:${APP_NAME} --chmod=750 ${APP_NAME} /home/${APP_NAME}
COPY --from=builder --chown=${APP_NAME}:${APP_NAME} --chmod=750 /home/${APP_NAME}/.venv .venv


EXPOSE 8000
USER ${APP_NAME}
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
