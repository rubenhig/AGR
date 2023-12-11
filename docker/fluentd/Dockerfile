FROM fluent/fluentd:v1.12-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.0.3"]

COPY ep_fluentd.sh /ep_fluentd.sh

RUN chmod +x /ep_fluentd.sh