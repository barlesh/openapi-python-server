#! /bin/bash

# run docker compose with application service and tester
docker-compose --env-file test-docker.env -f docker-compose.yml up 