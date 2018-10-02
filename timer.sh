# Add this to your ~/.bash_profile and then you can say countdown at terminal.
countdown(){
	echo "Enter Countdown time in seconds"
	read secs
	t1=(`date +%s`);
	while true;do
		t2=(`date +%s`)
		echo -ne "$((secs-t2+t1))\r"
		if [ "$((secs-t2+t1))" -le 0 ]
		then
			echo "TIME UP"
			say "Your $secs seconds are over. Countdown is over"
		fi
		sleep 0.1
	done
}
