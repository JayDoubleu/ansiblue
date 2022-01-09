#!/bin/bash 
executable=$(basename $0)
set -x
exec flatpak-spawn --host --watch-bus --forward-fd=1 --forward-fd=2 --directory=$(pwd) --env=TERM=$TERM $executable "$@"

# Source: 
# https://github.com/containers/toolbox/issues/145#issuecomment-582040463
# https://github.com/containers/toolbox/pull/553/commits/48aa3e507f2c1f7ac742f1bb5ac20e53fbbec45c
