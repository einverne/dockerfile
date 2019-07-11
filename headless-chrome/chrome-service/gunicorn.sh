#!/bin/bash
cd / && gunicorn -w 4 -b 0.0.0.0:9223 server:app
