# energyPulseCounter

This project uses an arduino to count pulses from an energy meter (electricity)

the python script collects the data on serial, and pushes it to domoticz for graphing etc.

## Install instructions

Program your arduino with the sketch, and connect a ligth to voltage converter (LTS257).
I've used an arduino micro, connected the DO pin of the LTS257 to D3 on the micro, might be another
pin on other arduino variants (or modify the sketch to use another interrupt pin).

On your raspberry, put the python file into /usr/local/bin, and make it executable :

sudo cp pulseCount.py /usr/local/bin
sudo chmod +x /usr/local/bin/pulseCount.py

move the init script to /etc/init.d, and make it executable:

sudo cp pulseCount /etc/init.d
sudo chmod +x /etc/init.d/pulseCount

and finally add it to your startup :

sudo update-rc.d pulseCount defaults

connect the arduino to your pi, and restart it.

