# NOTE: NPM packages for integration/contract testing pull in vendored
# glibc-linked binaries. Do not use Alpine containers.
FROM node:14-buster-slim

WORKDIR /opt/main/client

COPY client/package.json /opt/main/client/package.json
COPY client/package-lock.json /opt/main/client/package-lock.json

RUN npm ci

RUN apt-get update && apt-get install -y \
    dumb-init \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/bin/bash"]

COPY client/public /opt/main/client/public
COPY client/src /opt/main/client/src
