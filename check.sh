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
./allbuild.sh > /dev/null
debug "done building"

WRONGS=""
RIGHTS=""

for Q in $QUESTIONS ; do
  EXEC="$Q/build/$Q"
  info "evaluating $EXEC"
  INFILE="$Q/input.txt"
  EXPECTEDFILE="$Q/expected-output.txt"
  if [ ! -f "$EXPECTEDFILE" ] ; then
    echo "file missing: $EXPECTEDFILE" >&2
    exit 1
  fi
  OUTFILE="$Q/build/actual.txt"
  if [ -f "$INFILE" ] ; then
    rm -rf ./screenlog.*
    SESSIONNAME=$(basename "$Q")
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
    dos2unix -q -n screenlog.0 "$OUTFILE"
    rm screenlog.0
  else
    echo "$Q: no input file" >&2
    "$EXEC" > "$OUTFILE"
  fi
  #ACTUAL=$(cat "$OUTFILE")
  #EXPECTED=$(cat "$EXPECTEDFILE")
  
  if diff "$EXPECTEDFILE" "$OUTFILE" ; then
    RIGHTS="$Q $RIGHTS"
  else
    WRONGS="$Q $WRONGS"
  fi
done

if [ -n "$WRONGS" ] ; then
  echo "wrong: $WRONGS" >&2
  exit 1
else
  echo "gravy: $RIGHTS"
fi
