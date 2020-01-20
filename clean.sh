#!/bin/bash

set -e

BUILD_DIR_NAME=$1

if [ -z "${BUILD_DIR_NAME}" ] ; then
  BUILD_DIR_NAME=build
fi

find . -type d -name "$BUILD_DIR_NAME" -print -exec rm -r {} \+
find . -type f -name "screenlog.*" -delete
