# syntax=docker/dockerfile:1.5

# Use the Bookworm slim variant which receives timely security updates
FROM python:3.11-slim-bookworm AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

FROM base AS builder
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential git && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM base AS runtime
LABEL maintainer="Phase0 Foundation Team"
# Apply latest security updates available in the base image and remove known vulnerable OS packages
RUN apt-get update && \
    apt-get -y upgrade && \
    # Remove PAM libraries where CVE-2025-6020 is reported (not needed in this container)
    apt-get purge -y --auto-remove libpam-modules libpam-modules-bin libpam-runtime libpam0g || true && \
    # Remove vulnerable sqlite runtime if not required by the app
    apt-get purge -y --auto-remove libsqlite3-0 || true && \
    rm -rf /var/lib/apt/lists/*
# Ensure vulnerable setuptools from base image is replaced with a fixed version
RUN python -m pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" wheel
# Avoid installing extra OS packages in runtime to reduce vulnerability surface
COPY --from=builder /install /usr/local
COPY src /app/src
COPY scripts /app/scripts
COPY docker/start.sh /app/scripts/start.sh
COPY scripts/healthcheck.py /app/scripts/healthcheck.py
RUN chmod +x /app/scripts/start.sh
RUN chmod +x /app/scripts/healthcheck.py
RUN groupadd --system appuser && useradd --system --gid appuser --create-home appuser
RUN chown -R appuser:appuser /app
USER appuser
ENV APP_ENV=development
ENV LOG_LEVEL=info
# Use Python for healthcheck to avoid curl dependency
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=5 CMD ["python","/app/scripts/healthcheck.py"]
CMD ["/app/scripts/start.sh"]
