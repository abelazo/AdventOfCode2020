#!/usr/bin/env bash

for i in $(cat $1); do
    for j in $(cat $1); do
        for k in $(cat $1); do
            sum=$(( $i + $j + $k ))
            if [ "$sum" == "2020" ]; then
                echo $i,$j,$k
            fi
        done
    done
done
