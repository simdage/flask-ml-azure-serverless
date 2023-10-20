#!/usr/bin/env bash
PORT=5000
echo "Port: $PORT"
# POST method predict
curl -d '[[1, 2, 3, 4], [0, 0, 0, 0]]'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict