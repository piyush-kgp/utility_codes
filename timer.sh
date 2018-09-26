echo "Countdown time in seconds"
read secs
t1=(`date +%s`);
while true;do
	t2=(`date +%s`)
	echo -ne "$((secs-t2+t1))\r"
	if [ "$((secs-t2+t1))" -le 0 ]
	then
		echo "TIME UP"
		say "Countdown over"
	fi
	sleep 0.1
done
