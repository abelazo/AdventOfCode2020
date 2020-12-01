#!/usr/bin/env bash

for i in $(cat $1); do
    for j in $(cat $1); do
	echo $(( 2020 - $i )),$j
    done
done | awk -F',' '($1 == $2) {print $1}'
