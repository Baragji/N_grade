# syntax=docker/dockerfile:1.5

FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

FROM base AS builder
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential git curl && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/requirements.txt
RUN pip install --prefix=/install -r requirements.txt || true

FROM base AS runtime
LABEL maintainer="Phase0 Foundation Team"
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*
COPY --from=builder /install /usr/local
COPY src /app/src
COPY scripts /app/scripts
COPY docker/start.sh /app/scripts/start.sh
RUN chmod +x /app/scripts/start.sh
RUN groupadd --system appuser && useradd --system --gid appuser --create-home appuser
RUN chown -R appuser:appuser /app
USER appuser
ENV APP_ENV=development
ENV LOG_LEVEL=info
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=5 CMD curl -f http://localhost:8000/health || exit 1
CMD ["/app/scripts/start.sh"]
