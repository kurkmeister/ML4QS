#!/bin/bash

set -e
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )/"

# docker build -t kurkmeister/ml4qs:base .
# docker push kurkmeister/ml4qs:base

docker run --rm -it -v "${PROJECT_DIR}:/root" kurkmeister/ml4qs:base

