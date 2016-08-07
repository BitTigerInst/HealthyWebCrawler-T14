#!/bin/bash
export $( cat .env-production|xargs)
mkdir dist
./node_modules/.bin/babel tools --out-dir dist --ignore "spec.js",
