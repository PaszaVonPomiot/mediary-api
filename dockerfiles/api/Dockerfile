FROM python:3.12-slim AS base

ARG APP_NAME
ENV PATH=/home/${APP_NAME}/.venv/bin:$PATH

RUN find /etc/skel -type f -name ".*" -delete \
    && useradd --home-dir /home/${APP_NAME} --comment "Application User" \
    --shell /usr/sbin/nologin ${APP_NAME}
WORKDIR /home/${APP_NAME}

# ------------------------------------------------------------------------------

FROM base AS builder

COPY ${APP_NAME} ./requirements.txt ./
RUN pip install uv && \
    uv venv /home/${APP_NAME}/.venv && \
    uv pip install -r requirements.txt

# ------------------------------------------------------------------------------

FROM base AS runner

COPY --from=builder --chown=${APP_NAME}:${APP_NAME} --chmod=750 /home/${APP_NAME}/.venv .venv
COPY --chown=${APP_NAME}:${APP_NAME} --chmod=751 ${APP_NAME} /home/${APP_NAME}

EXPOSE 8000
USER ${APP_NAME}
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
