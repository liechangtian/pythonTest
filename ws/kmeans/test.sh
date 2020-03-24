#!/usr/bin/env bash

files=`ls|awk '/^da/'`

for file in ${files} ; do
    echo ${file}
    newFile=`echo $file`
    echo $newFile
done
