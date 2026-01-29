FROM python:3.10-slim

WORKDIR /chroma

# Install chromadb + FastAPI + Uvicorn + OpenTelemetry deps
RUN pip install --no-cache-dir chromadb fastapi uvicorn \
    opentelemetry-api \
    opentelemetry-sdk \
    opentelemetry-instrumentation \
    opentelemetry-instrumentation-fastapi

EXPOSE 8000

CMD ["chroma", "run", "--host", "0.0.0.0", "--port", "8000"]