FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --no-cache-dir --upgrade "pip==26.2.2"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py ./main.py
COPY ./*.txt ./

CMD ["python", "main.py"]

# Exercise the installed runtime verifiers before an image can be published.
COPY scripts/verify_tls.py /usr/local/bin/verify-tls.py
RUN python /usr/local/bin/verify-tls.py
