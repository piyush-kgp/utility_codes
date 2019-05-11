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
# update /etc/ssmtp/ssmtp.conf a/c to https://unix.stackexchange.com/questions/36982/can-i-set-up-system-mail-to-use-an-external-smtp-server
# free -m | mail -s "memory usage" to@email.id
# you'll need to allow less secure apps in your account security options.
