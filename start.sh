#!/usr/bin/bash
# Creates sym links for easier manipulation of files

# Loading path form config
configPath=$HOME/.config/workoutPlan.conf
if [ -f $configPath ]
then
	source $configPath
else
	echo "No config file found to determine LOGPATH"
fi

# Selection menu
PS3="Select step: "
select step in Choose Time Log History Catalog Quit
do
	case $step in
		Choose)
			python3 $LOGPATH/1-choose.py
			;;
		Time)
			python3 $LOGPATH/2-time.py
			;;
		Log)
			python3 $LOGPATH/3-log.py
			;;
		History)
			bash $LOGPATH/history.sh
			;;
		Catalog)
			bash $LOGPATH/history.sh abc
			;;
		Quit)
			break
			;;
		*)
			echo "Invalid option"
			;;
	esac
done
