package main
// kbd-backlight is a small service that monitors evdev
// and turns up backlight on samsung laptop

import (
	"os"
	"fmt"
	"github.com/gvalkov/golang-evdev"
	"io/ioutil"
)


const (
	backlight_device = "/sys/devices/platform/samsung/leds/samsung::kbd_backlight/brightness"
	kbd_dev = "/dev/input/event3"
)

func main() {
  // TODO: check if we have we are run as root
	var kbd *evdev.InputDevice
	var events []evdev.InputEvent
	var err error
	lightness := []byte("3")
	kbd, err = evdev.Open(kbd_dev)
	if err != nil {
		fmt.Printf("Unable to open input device: %s\n. got root?", kbd_dev)
		os.Exit(1)
	}
//	fmt.Println(kbd)
	for {
		events, err = kbd.Read()
		for range events{
		//	fmt.Println(&events[i])
			fileerr := ioutil.WriteFile(backlight_device, lightness, 0644)
			if fileerr != nil {
				fmt.Printf("Unable to write to %s", backlight_device)
			}
		}
	}
}
