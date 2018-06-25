# Notes on my attempts to address some of the features that arent working with my samsung ATIV 9 Spin

I guess theres really just two key issues I have with this laptop. Both seem to relate to Keyboard. HA!

### Keyboard Backlight
Technically it works.

I can turn on the backlight like so.
```
echo 2 > /sys/devices/platform/samsung/leds/samsung::kbd_backlight/brightness
```

But it turns off again after about 3 seconds. I'm not sure what turns it off. Haven't found anything that is modifying that file.
Could be seen as a feature. If the backlight were triggered by key presses, you could have it dim when the keyboard is inactive.
That would require every keyboard event set the brightness. If it was properly event driven it could work.
But I don't know how I would go about doing that. Maybe it's dbus or udev or something.
Not familiar with keyboard events are handled.

The simplest hack I've found is to use a watch to bump the brightness every couple seconds.
```
watch su -c "echo 2 > /sys/devices/platform/samsung/leds/samsung::kbd_backlight/brightness"
```

Eventually I will turn that into some kinda of service. Unless I find something I've missed. But it could be a good project.

```
import evdev

backlight_device = '/sys/devices/platform/samsung/leds/samsung::kbd_backlight/brightness'
keybd = evdev.InputDevice('/dev/input/event3')

for event in keybd.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
                with open(backlight_device,'w') as b:
                        b.write('3')
```


The keys don't work. But they do register in dmesg. Haven't figured out how to utilize thats.
Not sure which keycodes I should be using.
```
atkbd serio0: Unknown key pressed (translated set 2, code 0xac on isa0060/serio0).
atkbd serio0: Use 'setkeycodes e02c <keycode>' to make it known.
atkbd serio0: Unknown key released (translated set 2, code 0xac on isa0060/serio0).
atkbd serio0: Use 'setkeycodes e02c <keycode>' to make it known.
atkbd serio0: Unknown key pressed (translated set 2, code 0xbb on isa0060/serio0).
atkbd serio0: Use 'setkeycodes e03b <keycode>' to make it known.
atkbd serio0: Unknown key released (translated set 2, code 0xbb on isa0060/serio0).
atkbd serio0: Use 'setkeycodes e03b <keycode>' to make it known.
```

## Tablet Mode
The Keyboard and touchpad should disable when in tablet mode. This does not happen.
There should probably be (maybe there is) an even that indicates the screen has folded back.
Is it a sensor in the hinge? Or maybe a magnet in the base?

I might have to manually disable kb/touchpad. Seems straight forward. Just need to make it accessible by touch.

Found this on StackExchange or something. (Should probably have links as I'm discovering info).
```
# disable
xinput float <device>

# enable
xinput reattach <device> <master>
```

xinput also has a `--disable`` option need to research the difference there.


sudo lsinput
sudo input-events
sudo input-kbd
