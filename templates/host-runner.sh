#!/bin/bash 
executable=$(basename $0)
set -x
exec flatpak-spawn --host $executable "$@"

# Source: https://github.com/containers/toolbox/issues/145#issuecomment-582040463
