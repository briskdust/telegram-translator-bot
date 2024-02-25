FROM python:3.10-rc-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update \
    && apt install -y --no-install-recommends gcc libffi-dev g++ \
    && pip install -r requirements.txt \
    && apt purge -y --auto-remove gcc libffi-dev g++ \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]
