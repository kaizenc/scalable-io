build: FORCE \
	build-server \
	build-client

build-server: FORCE
	docker build -t ghcr.io/kaizenc/scalable-io:latest -f conf/server/Dockerfile .

build-client: FORCE
	docker build -t ghcr.io/kaizenc/scalable-io-client:latest -f conf/client/Dockerfile .

pull: FORCE
	docker pull ghcr.io/kaizenc/scalable-io:latest

push: FORCE
	docker push ghcr.io/kaizenc/scalable-io:latest

up: FORCE
	docker compose -p kaizenc up -d --no-build server

client-up: FORCE
	docker compose -p kaizenc up -d --no-build client

down: FORCE
	docker compose -p kaizenc down -v

FORCE:  # https://www.gnu.org/software/make/manual/html_node/Force-Targets.html#Force-Targets