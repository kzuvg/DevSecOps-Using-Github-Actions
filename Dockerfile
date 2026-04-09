FROM pythonL3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirment.txt

EXPOSE 80
