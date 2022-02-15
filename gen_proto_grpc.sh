#!/usr/bin/env bash

set -eux

PROJECT_HOME=/Users/azb/VSCProjects/bazelbox/appletree
/Users/azb/.pyenv/versions/otel/bin/python3.8 -m grpc_tools.protoc -I$PROJECT_HOME --python_out=$PROJECT_HOME --grpc_python_out=$PROJECT_HOME appletree.proto
