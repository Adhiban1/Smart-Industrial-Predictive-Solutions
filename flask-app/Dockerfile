FROM alpine:latest
WORKDIR /app
RUN apk update
RUN apk add python3 py3-flask
COPY . .
CMD ["python", "app.py"]
EXPOSE 5000