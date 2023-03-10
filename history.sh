#!/bin/bash
# Prints the exercise catalog by date. If an "abc" argument is passed, orders alfabetically.

if [[ $1 = "abc" ]]
then
	echo "Sorting alfabetically"
	t=""
else
	echo "Sorting by time"
	t="t"
fi

ls -ogl$t --time-style=long-iso log --hide="day.csv"
