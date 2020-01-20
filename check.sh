#!/bin/bash

set -e

if [ "$DEBUG" == "1" ] ; then
  DEBUGSINK="/dev/stderr"
else
  DEBUGSINK="/dev/null"
fi

debug()
{
  echo "debug: $1 $2 $3 $4 $5" >$DEBUGSINK
}

info()
{
  echo "info: $1 $2 $3 $4 $5" >/dev/stderr
}

PAUSE="${PAUSE:-0.1}"

if [ -z "$1" ] ; then
  QUESTIONS=$(ls -d q?)
  debug "QUESTIONS=$QUESTIONS"
else
  QUESTIONS=$1
fi

debug "building..."
./build.sh > /dev/null
debug "done building"

WRONGS=""
RIGHTS=""

for Q in $QUESTIONS ; do
  BUILD_DIR="$Q/cmake-build"
  EXEC="$BUILD_DIR/$Q"
  info "evaluating $EXEC"
  INFILE="$Q/input.txt"
  EXPECTEDFILE="$Q/expected-output.txt"
  if [ ! -f "$EXPECTEDFILE" ] ; then
    echo "file missing: $EXPECTEDFILE" >&2
    exit 1
  fi
  OUTFILE="$BUILD_DIR/actual.txt"
  touch "$OUTFILE"
  truncate --size=0 "$OUTFILE"
  if [ -f "$INFILE" ] ; then
    if [ "$(wc -l < "$INFILE")" == "0" ] ; then
      echo "must contain newline: $INFILE" <&2
      exit 1
    fi
    rm -rf ./screenlog.*
    TEMPFILE=$(mktemp --tmpdir="$BUILD_DIR" sess_XXXXXXXXX)
    SESSIONNAME=$(basename "$TEMPFILE")
    screen -L -S "$SESSIONNAME" -d -m "$EXEC"
    debug "sleeping ${PAUSE} after opening screen session $SESSIONNAME"
    sleep "$PAUSE"
    while IFS= read -r line
    do
      screen -S "$SESSIONNAME" -X stuff "$line
"
      debug "sleeping ${PAUSE} after entering $line"
      sleep "$PAUSE"
    done < "$INFILE"
    screen -S "$SESSIONNAME" -X quit >/dev/null || true 
    rm "$TEMPFILE" -f
    dos2unix -q -n screenlog.0 "$OUTFILE"
    rm screenlog.0
  else
    echo "$Q: no input file" >&2
    "$EXEC" > "$OUTFILE"
  fi
  
  if diff "$EXPECTEDFILE" "$OUTFILE" ; then
    RIGHTS="$Q $RIGHTS"
  else
    WRONGS="$Q $WRONGS"
  fi
done

if [ -n "$WRONGS" ] ; then
  echo "wrong: $WRONGS" >&2
  exit 2
else
  echo "gravy: $RIGHTS"
fi
