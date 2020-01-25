#!/bin/bash

set -e

command -V screen >/dev/null
command -V dos2unix >/dev/null

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
  INFILES=$(find "$Q" -type f -name "input*.txt" -print0 | sort -z | xargs -0 echo)
  debug "input files: $INFILES"
  for INFILE in $INFILES ; do
    ANY_INPUT=1
    if [ "$(wc -l < "$INFILE")" == "0" ] ; then
      echo "input file must contain newline: $INFILE" <&2
      exit 1
    fi
    INFILE_BASE=$(basename "$INFILE")
    SUFFIX=${INFILE_BASE:5}
    EXPECTEDFILE="$Q/expected-output${SUFFIX}"  # input-3.txt -> expected-output-3.txt
    info "test case: $INFILE -> $EXPECTEDFILE"
    if [ ! -f "$EXPECTEDFILE" ] ; then
      echo "file missing: $EXPECTEDFILE" >&2
      exit 1
    fi
    OUTFILE="$BUILD_DIR/actual${SUFFIX}.txt"
    touch "$OUTFILE"
    truncate --size=0 "$OUTFILE"
    rm -rf ./screenlog.*
    TEMPFILE=$(mktemp --tmpdir="$BUILD_DIR" sess_XXXXXXXXX)
    SESSIONNAME=$(basename "$TEMPFILE")
    screen -L -S "$SESSIONNAME" -d -m "$EXEC"
    debug "sleeping ${PAUSE} after opening screen session $SESSIONNAME"
    sleep "$PAUSE"
    while IFS= read -r line
    do
      # Notice the line break in the line that follows
      screen -S "$SESSIONNAME" -X stuff "$line
"
      debug "sleeping ${PAUSE} after entering $line"
      sleep "$PAUSE"
    done < "$INFILE"
    screen -S "$SESSIONNAME" -X quit >/dev/null || true
    rm "$TEMPFILE" -f
    dos2unix -q -n screenlog.0 "$OUTFILE"
    rm screenlog.0
    if diff "$EXPECTEDFILE" "$OUTFILE" ; then
      RIGHTS="$Q $RIGHTS"
    else
      WRONGS="$Q $WRONGS"
    fi
    if [ "$FIRST" == "1" ] ; then
      break
    fi
  done
  if [ -z "$ANY_INPUT" ] ; then
    echo "$Q: no input files" >&2
    "$EXEC" > "$OUTFILE"
    EXPECTEDFILE="$Q/expected-output.txt"
    if diff "$EXPECTEDFILE" "$OUTFILE" ; then
      RIGHTS="$Q $RIGHTS"
    else
      WRONGS="$Q $WRONGS"
    fi
  fi
done

if [ -n "$WRONGS" ] ; then
  echo "wrong: $WRONGS" >&2
  exit 2
else
  echo "gravy: $RIGHTS"
fi
