FROM ubuntu:latest
WORKDIR /app
RUN apt update
RUN apt install python3 python3-venv -y
COPY requirements.txt .
RUN python3 -m venv venv
RUN ./venv/bin/pip install -r requirements.txt
COPY . .
CMD ["./venv/bin/python3", "app.py"]
EXPOSE 5000