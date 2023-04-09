#!/bin/bash
# Prints the exercise catalog by date. If an "abc" argument is passed, orders alfabetically.

if [[ $1 = "abc" ]]
then
	echo "Sorting alfabetically"
	tree log -i --dirsfirst
else
	echo "Sorting by time"
	tree log/ -t --timefmt "%a %d-%b" --noreport
fi
