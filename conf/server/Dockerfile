FROM python:3.9-slim-buster

WORKDIR /opt/main

RUN apt-get update && apt-get install -y \
    dumb-init \
    && rm -rf /var/lib/apt/lists/*

COPY conf/requirements.txt /opt/main/conf/requirements.txt
RUN pip install -r "/opt/main/conf/requirements.txt" \
    && rm -rf /root/.cache/pip/

COPY server /opt/main/server/

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/bin/bash"]
