# Use Python 3.14 slim image
FROM python:3.14-slim-trixie


# Install uv
#RUN pip install --no-cache-dir uv
RUN apt-get update && apt-get install -y --no-install-recommends curl pipx

RUN pipx install uv
RUN pipx ensurepath

WORKDIR /app
# Copy project configuration
COPY pyproject.toml .

# Install dependencies using uv
#RUN uv pip install --system .

# Copy application code
COPY app.py .
#COPY tests/ ./tests/

RUN /root/.local/bin/uv sync

# Create non-root user for security
#RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
#USER appuser

# Expose port
EXPOSE 8000

# Health check using Python (no need for curl)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/', timeout=5)" || exit 1

# Run application with uv
CMD ["/root/.local/bin/uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
