#!/bin/bash

output=`hg diff -r tip | grep 'local_test = true'`
if [ "${output}" != "" ]; then
    echo ${output}
    exit 1
fi
