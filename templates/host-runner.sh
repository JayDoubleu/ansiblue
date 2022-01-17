#!/bin/bash 
executable=$(basename $0)
export PATH=$HOME/.local/bin/:$PATH
set -x
exec sockpty $executable $@
