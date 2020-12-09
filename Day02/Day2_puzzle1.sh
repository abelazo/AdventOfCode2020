#!/usr/bin/env bash

trim_string() {
    # Usage: trim_string "   example   string    "
    : "${1#"${1%%[![:space:]]*}"}"
    : "${_%"${_##*[![:space:]]}"}"
    printf '%s\n' "$_"
}

IFS=''
cat $1 |
    while read line; do
	key=$(echo $line | cut -d ':' -f 1)
	dirtyPassword=$(echo $line | cut -d ':' -f 2)
	password=$(trim_string $dirtyPassword)
	
	min=$(echo $key | cut -d '-' -f 1)
	max=$(echo $key | cut -d '-' -f 2 | cut -d ' ' -f 1)
	char=$(echo $key | cut -d '-' -f 2 | cut -d ' ' -f 2)

	numOccurrences=$(echo $password | grep -o $char | wc -l)

	if [[ $numOccurrences -ge $min && $numOccurrences -le $max ]]; then
	    echo $line
	fi
    done
