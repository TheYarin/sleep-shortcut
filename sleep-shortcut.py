import keyboard
import ctypes

def putComputerToSleep():
    ctypes.windll.PowrProf.SetSuspendState(0, 0, 0)

keyboard.add_hotkey("F19+F17", putComputerToSleep)
keyboard.wait()