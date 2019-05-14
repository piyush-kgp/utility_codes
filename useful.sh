# Add this to your ~/.bash_profile and then you can say countdown at terminal.
countdown(){
	echo "Enter Countdown time in seconds"
	read secs
	t1=(`date +%s`);
	t2=(`date +%s`);
	speak_interval=30;
	while [ "$((t1+secs-t2))" -ge 0 ];do
		t2=(`date +%s`)
		echo -ne "*************************"
		echo -ne "$((secs-t2+t1)) seconds remaining"
		echo -ne "*************************\r"
		sleep 0.01
	done
	say "Countdown is over"
	while true;do
		t2=(`date +%s`)
		late=$((-secs+t2-t1))
		mod=$((late % speak_interval))
		echo -ne "####################"
		echo -ne "Countdown over. Running $((-secs+t2-t1)) seconds late"
		echo -ne "####################\r"
		if [ $((mod)) -le 2 ]
		then
			say "Countdown over. Running $((-secs+t2-t1)) seconds late"
		fi
		sleep 0.01
	done
}

stopwatch(){
	echo "Stopwatch Started"
	t1=(`date +%s`);
	while true;do
		t2=(`date +%s`)
		echo -ne "*************************"
		echo -ne "$((t2-t1)) Seconds gone"
		echo -ne "*************************\r"
		sleep 0.1
	done
}

InternetConnectionCheck(){
	#!/bin/bash
        wget -q --spider http://google.com
	if [ $? -eq 0 ]
	then
		ip=$(curl ifconfig.me)
		echo "Online with IP $ip"
	else
		echo "Offline"
	fi
}

testInternetSpeed(){
	curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -
}

# mailing
# apt-get install mailutils ssmtp
# update your file at /etc/ssmtp/ssmtp.conf as per instructions from https://unix.stackexchange.com/questions/36982/can-i-set-up-system-mail-to-use-an-external-smtp-server
# echo "test message" | mail -s "test msg" to@email.id
# you'll need to allow less secure apps in your google account security options.

# To do monitoring such as send a mail whenever ram usage crosses 90%, check every 5 minutes:
# your bash script should read from /proc/meminfo and look at the fields MemTotal and MemFree. Calculate ram usage, then 
# create the mail body and use the `mail` command to send mail. Schedule it on your cron as */5 * * * * *


# git add, commit and push
# # for some reason this doesnt work so I had to do it in a function
# alias cps="git add . && git commit -m \"$1\" && git push -u origin master"

cpsh(){
	echo "Enter commit message"
	read "msg"
	commit_msg="\"$msg\""
	cmd="git add . && git commit -m $commit_msg && git push -u origin master"
	eval $cmd
}
