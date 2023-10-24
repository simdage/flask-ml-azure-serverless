#!/usr/bin/env bash
PORT=8080
echo "Port: $PORT"
# POST method predict
curl -d '[[1, 2, 3, 4], [0, 0, 0, 0]]'\
     -H "Content-Type: application/json" \
     -X POST https://image-ply26agq5q-uc.a.run.app/predict