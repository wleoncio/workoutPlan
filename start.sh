#!/usr/bin/bash
# Creates sym links for easier manipulation of files

PS3="Select step: "
select step in Choose Time Log History Quit
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
		Quit)
			break
			;;
		*)
			echo "Invalid option"
			;;
	esac
done
