#!/usr/bin/env python
import evdev
import sys
import signal
import time

backlight_device = '/sys/devices/platform/samsung/leds/samsung::kbd_backlight/brightness'
keybd = evdev.InputDevice('/dev/input/event3')
config_file='/etc/sysconfig/kbd-backlight'
mode = 'event'


def sig_handler(signal,frame):
	print('SIGINT recieved')
	sys.exit(0)

def load_config():
	try:
		with open(config_file) as c:
			#parse config
			print('parsing config')
	except:
		print('couldnt load config. going with defaults')

def alwayson():
	print('alwayson')
	while True:
		with open(backlight_device,'w') as b:
			b.write('3')
		time.sleep(1)

def alwaysoff():
	print('why would you want it off? just turn off the service...')

def event():
	print('event mode')
#Just a loop
	for event in keybd.read_loop():
		if event.type == evdev.ecodes.EV_KEY:
			with open(backlight_device,'w') as b:
				b.write('3')


def main():
	event()

if __name__ == "__main__":
	signal.signal(signal.SIGINT,sig_handler)
        load_config()
	main()
