#!/bin/bash
set -e

./install.sh

sleep 2
echo "[run.sh] Listing running containers:"
docker ps

echo "[run.sh] Backend service should now be accessible at http://localhost:8000"
