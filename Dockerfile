FROM python:3.10-slim

# Install Chrome dependencies for Selenium
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libgdk-pixbuf2.0-0 \
    libxrandr2 \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgtk-3-0 \
 && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy all source files
COPY . .

# Set the Python path so `src/` is on sys.path
ENV PYTHONPATH="/app/src"

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI (if using uvicorn in server mode)
EXPOSE 10000

# Run the app — `main.py` is in the root and imports from src/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
