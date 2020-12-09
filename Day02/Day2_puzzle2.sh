#!/usr/bin/env bash

trim_string() {
    # Usage: trim_string "   example   string    "
    : "${1#"${1%%[![:space:]]*}"}"
    : "${_%"${_##*[![:space:]]}"}"
    printf '%s\n' "$_"
}

case1=$(mktemp)
case2=$(mktemp)

IFS=''
cat $1 |
    while read line; do
	key=$(echo $line | cut -d ':' -f 1)
	dirtyPassword=$(echo $line | cut -d ':' -f 2)
	password=$(trim_string $dirtyPassword)
	
	pos1=$(echo $key | cut -d '-' -f 1)
	pos2=$(echo $key | cut -d '-' -f 2 | cut -d ' ' -f 1)
	char=$(echo $key | cut -d '-' -f 2 | cut -d ' ' -f 2)

	i=$(( $pos1 - 1 ))
	j=$(( $pos2 - 1 ))

	occ1=${password:$i:1}
	occ2=${password:$j:1}

	[ "$occ1" == "$char" ] && [ "$occ2" != "$char" ] && echo $line >> $case1
	[ "$occ1" != "$char" ] && [ "$occ2" == "$char" ] && echo $line >> $case2
    done

cat $case1 $case2 # Union
rm $case1 $case2
