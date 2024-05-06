import os
import time
#simple bomb that will loop forever creating yes processes and eating up CPU, added a sleep to give my IDPS a little more leeway.
def bomb():
     while True:
            os.system("yes > /dev/null &")
            time.sleep(0.5)

if __name__ == "__main__":
    bomb()
