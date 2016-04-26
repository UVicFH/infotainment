#!/bin/bash
: '

Hello Adam, please follow these steps

run:

	sudo vi /etc/inittab

comment out this line:

	1:2345:respawn:/sbin/getty 115200 tty1

so it should now be

	#1:2345:respawn:/sbin/getty 115200 tty1

then add below the commented line

	1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1

then save and exit

reboot the pi

	sudo reboot

now it should log you in all sweet like :3

now to add this boot script so we start our gui everytime do the following

	sudo vi /etc/profile

add this line to the end of the file

	. /home/pi/startup.sh

then save and exit

reboot the pi and message marc the output.

'

sudo ip link set can0 type can bitrate 500000
echo "CAN initiated at can0"
echo "Starting Infotainment"
#sudo python3 /home/pi/Documents/PyQt_WIP/PyQt/MainApplication.py
sudo python3 /home/pi/UVicFH2016/MainApplication.py
