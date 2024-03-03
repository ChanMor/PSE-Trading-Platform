#!/bin/bash

cd /api
python -m uvicorn main:app &

cd /web
xdg-open index.html
