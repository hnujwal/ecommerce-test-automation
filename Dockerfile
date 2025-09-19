FROM python:3.12-slim

WORKDIR /app

# Install Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Set display for headless Chrome
ENV DISPLAY=:99

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY tests/ ./tests/
COPY pytest.ini .

# Create reports directory
RUN mkdir -p tests/reports

CMD ["python", "-m", "pytest", "tests/", "--html=tests/reports/report.html", "--self-contained-html", "-v"]