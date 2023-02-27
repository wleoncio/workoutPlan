#!/usr/bin/bash
# Creates sym links for easier manipulation of files

PS3="Select step: "
select step in Choose Time Log History Finish
do
	case $step in
		Choose)
			python3 1-choose.py
			;;
		Time)
			python3 2-time.py
			;;
		Log)
			python3 3-log.py
			;;
		History)
			bash history.sh
			;;
		Finish)
			python3 4-finish.py
			break
			;;
		*)
			echo "Invalid option"
			;;
	esac
done
