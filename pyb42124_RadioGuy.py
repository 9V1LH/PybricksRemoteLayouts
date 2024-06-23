## Pybricks Routine for LEGO DC App-Controlled Batmobile (Set 76112)
## Credit to Technicmaster0 (https://github.com/Tcm0/PybricksRemoteLayouts/)
##  and Profinerd (https://www.profinerd.de/2022/03/24/pybricks-tutorial-42140-mit-lego-fernbedienung-aber-ohne-handy-steuern-wie-genial-ist-das-denn/)
## Authored by Radio_guy on June 23, 2024
##
## Remote conrtol functions:
##  Left Plus (+): Drive forward
##  Left Center: Toggle speed
##  Left Minus (-): Drive backwards
##  Right Plus (-): Steer right
##  Right Plus (-): Steer left

from pybricks.hubs import TechnicHub
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait

# Initialize hardware components
print("Initialize hardware components")
hub = TechnicHub()
battstand = hub.battery.current()
battstand = str(battstand)
print("Battery status: " + battstand + "%")
hub.light.on(Color.ORANGE)
steering = Motor(Port.B)
driving = Motor(Port.A)

# Steering calibration sequence
steering.run_until_stalled(500)
steering.reset_angle(0)
steering.run_until_stalled(-500)
maxAngle = steering.angle()
steering.run_target(500, (maxAngle/2)+10)
steering.reset_angle(0)
hub.light.on(Color.RED)

# Connect the remote control and assign a name
print("Waiting for the Remote Control to connect ...")
remoteControl = Remote(timeout=10000)
try:
    print("Remote Control connected!")
    hub.light.blink(Color.GREEN, [50,500,50,500])
    wait(2000)
    remoteControl.name("pyb42124")

    hub.light.on(Color.BLUE*0.5)
    print("Ready for action!")

    # Maximum speed selection
    maxspeed = [40,80,100] # Define your maximum speed here
    s = 0
    speed_pressed = False

    # Main loop
    while True:
        # Update the pressed buttons information
        pressed = remoteControl.buttons.pressed()

        # Commands to drive forward or backward
        if Button.LEFT_MINUS in pressed:
            driving.dc(maxspeed[s])
        elif Button.LEFT_PLUS in pressed:
            driving.dc(-maxspeed[s])
        else: 
            driving.brake()

        # Toggle max. speed
        if Button.LEFT in pressed and not speed_pressed:
            if s < len(maxspeed) -1:
                s += 1
            else:
                s = 0
            print("Max. speed set to:" + str(maxspeed[s]))
            speed_pressed = True
        else:
            speed_pressed = False

        # Commands to steer the vehicle
        if Button.RIGHT_MINUS in pressed:
            steering.run_target(1200, (maxAngle/2)-5, Stop.HOLD,False)
        elif Button.RIGHT_PLUS in pressed:
            steering.run_target(1200, -((maxAngle/2)-5), Stop.HOLD,False)
        else:
            steering.run_target(1200, 0, Stop.HOLD, False)

        # Shut down the hub using the remote control
        if Button.CENTER in pressed:
            print("System shutdown requested by remote corntrol. Bye!")
            hub.light.blink(Color.RED, [50,50,50,50])
            wait(2000)
            hub.system.shutdown()

        wait(100)

# Shut down the system if no remote is connected within the timeout period
except OSError:
    print("Could not find the remote, switching off!")
    hub.light.blink(Color.RED, [50,50,50,50])
    wait(2000)
    hub.system.shutdown()
    exit()
