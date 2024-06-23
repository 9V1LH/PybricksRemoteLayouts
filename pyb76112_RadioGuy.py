## Pybricks Routine for LEGO DC App-Controlled Batmobile (Set 76112)
## Credit to Technicmaster0 (https://github.com/Tcm0/PybricksRemoteLayouts/)
##  and Profinerd (https://www.profinerd.de/2022/03/24/pybricks-tutorial-42140-mit-lego-fernbedienung-aber-ohne-handy-steuern-wie-genial-ist-das-denn/)
## Authored by Radio_guy on June 22, 2024

from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Remote
from pybricks.parameters import Button, Color, Port
from pybricks.tools import wait

# Initialize hardware components
print("Initialize hardware components")
hub = CityHub()
battstand = hub.battery.current()
battstand = str(battstand)
print("Battery status: " + battstand + "%")
driving = DCMotor(Port.B)
driving2 = DCMotor(Port.A)

# Connect the remote control and assign a name
remoteControl = Remote(timeout=None)
print("Remote Control connected!")
hub.light.blink(Color.GREEN, [50,500,50,500])
wait(2000)
remoteControl.name("pyb76112")

hub.light.on(Color.RED*0.5)
print("Ready for action!")

# main loop
while True:
    # Update the information on pressed buttons
    pressed = remoteControl.buttons.pressed()

    # Commands to drive the vehicle forward or backward
    if Button.LEFT_PLUS in pressed and Button.RIGHT_PLUS in pressed:
        driving.dc(-100)
        driving2.dc(100)
    elif Button.LEFT_MINUS in pressed and Button.RIGHT_MINUS in pressed:
        driving.dc(100)
        driving2.dc(-100)
    elif Button.LEFT_PLUS in pressed and Button.RIGHT_MINUS in pressed:
        driving.dc(-100)
        driving2.dc(-100)
    elif Button.LEFT_MINUS in pressed and Button.RIGHT_PLUS in pressed:
        driving.dc(100)
        driving2.dc(100)
    elif Button.LEFT_PLUS in pressed:
        driving.dc(-100)
    elif Button.LEFT_MINUS in pressed:
        driving.dc(100)
    elif Button.RIGHT_PLUS in pressed:
        driving2.dc(100)
    elif Button.RIGHT_MINUS in pressed:
        driving2.dc(-100)

    # Perform a wheelie when the left button is pressed
    elif Button.LEFT in pressed:
        driving.dc(100)
        driving2.dc(-100)
        wait(300)
        driving.dc(-100)
        driving2.dc(100)
        wait(500)

    # Turn backward when the right button is pressed
    elif Button.RIGHT in pressed:
        driving.dc(100)
        driving2.dc(100)
        wait(500)
        driving.dc(-100)
        driving2.dc(-100)
        wait(800)
        driving.dc(100)
        driving2.dc(100)
        wait(700)
        driving.dc(-100)
        driving2.dc(-100)
        wait(1400)

    # Shut down the hub using the remote control
    elif Button.CENTER in pressed:
        print("System shutdown requested by remote control. Bye!")
        hub.light.blink(Color.RED, [50,50,50,50])
        wait(2000)
        hub.system.shutdown()

    # Stop both motors
    else: 
        driving.brake()
        driving2.brake()
    wait(100)
