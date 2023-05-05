import LCDlibrary
import time

def setup(Val1="", Val2="", Val3="", Val4=""):
    LCDlibrary.init(0x27, 1)    # init(slave address, background light)
    LCDlibrary.write(0, 0, Val1)
    LCDlibrary.write(0, 1, Val2)
    LCDlibrary.write(0, 2, Val3)
    LCDlibrary.write(0, 3, Val4)
    time.sleep(2)
    
def destroy():
    LCDlibrary.clear()

if __name__ == "__main__":
    try:
        setup()
    except KeyboardInterrupt:
        destroy()

