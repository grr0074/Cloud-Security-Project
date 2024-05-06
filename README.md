## README Host Based Attack (Bomb) and IDPS: 

Requirements:

- Python 3.x
- `psutil` library (install with `pip install psutil`)

## IDPS Portion: IDPS.py

This a python script that will monitor the VM's resources, detech whenever an attack is occuring and then promptly prevent said attack from harming the VM

How to run:

1.Save the script as a python file with a .py ending
2. Open a terminal and navigate to the correct directory that contains the script
3. Run the script using the following command

python3 IDPS.py

Expected Behavior:

It will continously print the current CPU || Memory || Current Amount of running processes so you can visually see how the VM is doing and the effect the bomb has, CPU, Memory and Process thresholds are set and if they are crossed that means an attack is occuring

When a bomb is detected it will be printed to the screen that it is detected and then once the maximum process threshold for a certain kind is crossed processes will start to be eliminated. 

This will run indefenitley thwarting the attack for as long as you like, allowing you to save your data // alert an admin // figure out where this attack is coming from

After 20 iterations of the loop, The user will be prompted if they want to restart the VM to escape the attack, make sure you are a superuser as SUDO is required

Customization:

You can set the thresholds to fit your machine and mold it around your machines normal behavior by setting the thresholds accordingly

## Bomb Attack Portion : Bomb.py 

How to Run:

1.Save the script as a python file with a .py ending
2. Open a terminal and navigate to the correct directory that contains the script
3. Run the script using the following command

python3 Bomb.py

Expected Behavior:

The command that the bomb is repeating will continous send the yes command to the /dev/NULL file, which send large amounts of strings to just be discarded. This takes up alot of the CPU and will lead to an eventual DDOS uninterrupted

The IDPS will make it so that the VM will never crash and everything is usuable while the attack is running

Exit out of terminal to stop the attack
