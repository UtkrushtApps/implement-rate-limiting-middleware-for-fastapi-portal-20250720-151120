#!/bin/bash
set -e

echo "[install.sh] Building Docker images..."
docker-compose build

echo "[install.sh] Starting backend service..."
docker-compose up -d

echo "[install.sh] Environment setup complete."
