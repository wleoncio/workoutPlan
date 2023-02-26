#!/usr/bin/bash
# Creates sym links for easier manipulation of files

PS3="Select step: "
select step in Choose Time Log History Finish
do
	case $step in
		Choose)
			python 1-choose.py
			;;
		Time)
			python 2-time.py
			;;
		Log)
			python 3-log.py
			;;
		History)
			bash history.sh
			;;
		Finish)
			python 4-finish.py
			break
			;;
		*)
			echo "Invalid option"
			;;
	esac
done
