# SB-Serial-Expansion-Hat
A Serial Expansion HAT with i2c Interface, Provides 2-channel UART (ttySC0 and ttySC1) along with 8 GPIOs.

<img src="/images/product_pic.png" height="300" width="400" />
<img src="/images/product_pic2.png" height="300" width="400" />

## Features :
* Compatible with Raspberry Pi Zero/Zero W/Zero WH/2B/3B/3B+/4B
* Onboard SC16IS752, expands 2-channel UART and 8 programmable GPIO through I2C
* It is stackable up to 16 modules by setting the address jumper A0 and A1, that means up to 32-channel UART
* Onboard Leds to indicate UART working status 

## Specifications : 
* Operating voltage: 3.3V
* Expansion chip: SC16IS752
* Control interface: I2C
* Dimension: 65mm x 30mm
* Mounting hole size: 2.8mm

### i2c Address setting
I2C device address can be configured by changing status of A0 and A1, that is by soldering
or by soldering 0 ohm resistor to them according to this table:

![GitHub Logo](/images/i2c_address_setting.PNG)

The I2C address in table are 8bits, however, the actual address is 7bits, you need to right-shift one bit to get the actual I2C address.
For example, if you connect A1 and A0 to Vdd, the address of module is 0x90 according to the table, to get the actual address
right-shift the data from 1001 000X to 100 1000, that is 0x48.

【Note】This module A0 and A1 are default welded to 3.3V, with I2C address 0x48

### How to Configure ?

#### Libraries Installation

* Install Python Libraries

```sudo apt-get install python-dev ```

```sudo apt-get install python-smbus ```

```sudo apt-get install python-spidev ```

#### Enable i2c Interface

1. Execute command: sudo raspi-config

2. Choose: Interfacing Options->I2C->Yes

![GitHub Logo](/images/i2c_enable1.PNG)

![GitHub Logo](/images/i2c_enable2.PNG)

3. Append this line to end of /boot/config.txt file, execute command:
```
sudo nano /boot/config.txt
```
and paste this line

```
dtoverlay=sc16is752-i2c,int_pin=24,addr=0x48
# addr is different according to status of A0/A1, default 0X48
```
4. Reboot
```
sudo reboot
```
5. After rebooting, you can execute command: ls /dev/ to check if SC16IS752 has been enabled to kernel.

![GitHub Logo](/images/ls_dev.png)

6. You can also execute below command to find out connected i2c device address :
```
sudo i2cdetect -y 1
```

### How to run examples
 1. Clone this git repository by executing command 
 
 ```
 git clone https://github.com/sbcshop/SB-Serial-Expansion-Hat.git
 ```
 2. open examples folder and edit UART interface on code as per your need (ttySC0 or ttySC1).
 
 3. Now type below command to run it.
 ```
 sudo python3 send.py
 ```
 OR
 ```
  sudo python3 receive.py
  ```






