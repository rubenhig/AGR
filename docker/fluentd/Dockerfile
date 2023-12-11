FROM fluent/fluentd:v1.12-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.0.3"]

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh