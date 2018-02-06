#!/bin/bash

output=`hg status | grep '^\? '`
if [ "${output}" != "" ]; then
    echo ${output}
    exit 1
fi
