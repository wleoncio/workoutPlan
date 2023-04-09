#!/bin/bash
# Prints the exercise catalog by date. If an "abc" argument is passed, orders alfabetically.

# Loading path form config
configPath=$HOME/.config/workoutPlan.conf
if [ -f $configPath ]
then
	source $configPath
else
	echo "No config file found to determine LOGPATH"
fi

# Printing log folder contents
if [[ $1 = "abc" ]]
then
	echo "Sorting alfabetically"
	tree $LOGPATH -i --dirsfirst
else
	echo "Sorting by time"
	tree $LOGPATH -t --timefmt "%a %d-%b" --noreport
fi
