# esp32-dashboard

This project uses ESP32 devices and various sensors to publish data to a server that is running on Render.

## ESP32 Todo
1. Setup secondary esp32 to send data to primary esp32 using esp-now
2. Have primary esp32 publish that data to the Render server
3. Connect light sensor to secondary esp32, and send the data with esp-now
4. Cleanup secondary esp32 wiring, make sure it all stays together
5. Move secondary esp32 to plant, setup to stay powered on
6. Setup temp+humidity sensor on third esp32 for setup
7. Move temp+humidity sensor to secondary esp32
8. Look into housing for the setup
9. Look into solar power for outdoor setup
10. Look into more sensors to use
11. Look into custom schamtic development (sensor 'hat' using i2c sensors)

## Web Dev Todo
1. Add page explaining setup (will change many times)
2. Look into logging data (on html or python side or both?)
3. Make it look prettier
4. Research what other companies have done
