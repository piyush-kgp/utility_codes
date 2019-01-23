# Add this to your ~/.bash_profile and then you can say countdown at terminal.
countdown(){
	echo "Enter Countdown time in seconds"
	read secs
	t1=(`date +%s`);
	t2=(`date +%s`);
	while [ "$((t1+secs-t2))" -ge 0 ];do
		t2=(`date +%s`)
		echo -ne "*************************"
		echo -ne "$((secs-t2+t1)) seconds remaining"
		echo -ne "*************************\r"
		sleep 0.01
	done
	while true;do
		t2=(`date +%s`)
		echo -ne "####################"
		echo -ne "Countdown over. Running $((-secs+t2-t1)) seconds late"
		echo -ne "####################\r"
		say "Countdown over. Running $((-secs+t2-t1)) seconds late"
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
