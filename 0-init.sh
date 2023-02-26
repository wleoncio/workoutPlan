#!/usr/bin/bash
# Creates sym links for easier manipulation of files

dest="$HOME/.local/bin"

touch "$dest" 1-choose.py

ln -s 1-choose.py "$dest"

PS3="Select step: "
select step in Choose Time Log Finish
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
		Finish)
			python 4-finish.py
			break
			;;
		*)
			echo "Invalid option"
			;;
	esac
done
