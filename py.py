import pyautogui
from time import sleep


def press_time(key, step, time = 0.0):
    pyautogui.keyDown(key)
    if (step == 1):
        step = 0
    if time == 0:
        if (step < 3):
            time =  0.10
        elif (step <= 5):
            time = 0.13
        elif (step > 5):
            time = 1/7
    sleep(time * step)
    pyautogui.keyUp(key)


def level1():
   press_time('right', 5)
   press_time('space', 0)
   press_time('right', 9)
   press_time('up', 2)

def level2():
    press_time('left', 1)
    press_time('up', 1)
    press_time('space', 0)

    press_time('left', 3)
    press_time('up', 1)
    press_time('space', 0)

    press_time('left', 5)
    press_time('up', 1)
    press_time('space', 0)

    press_time('left', 7)
    press_time('up', 1)
    press_time('space', 0)

    press_time('left', 3)
    press_time('down', 1)
    press_time('space', 0)

    press_time('left', 5)
    press_time('down', 1)
    press_time('space', 0)

    press_time('left', 9)
    press_time('up', 2)

def level3():
    press_time('down', 1)
    press_time('right', 5)
    press_time('down', 2)
    press_time('space', 0)

    press_time('down', 1)
    sleep(0.2)
    press_time('right', 5)
    press_time('down', 3)
    press_time('space', 0)

    press_time('down', 1)
    sleep(0.4)
    press_time('right', 5)
    press_time('down', 3)
    press_time('right', 7)
    press_time('up', 1)

def level4():
    press_time('right', 4)
    press_time('up', 1)
    press_time('E', 0)
    sleep(1)
    press_time('E', 0)
    sleep(0.5)
    press_time('space', 0)

    press_time('right', 8)
    press_time('up', 6)

def level5():
    press_time('left', 1)
    press_time('up', 1)
    sleep(1)
    press_time('E', 0)
    press_time('space', 0)

    press_time('right', 9)
    press_time('up', 2)

def level6():
    press_time('right', 2)
    press_time('up', 1)
    sleep(0.5)
    press_time('E', 0)
    press_time('space', 0)
    press_time('right', 6)
    press_time('up', 1)
    sleep(0.4)
    press_time('E', 0)
    press_time('space', 0)
    press_time('right', 9)
    press_time('up', 2)

def level7():
    press_time('up', 4)
    press_time('right', 2)
    for i in range(4):
        sleep(0.05)
        press_time('right', 2)
    press_time('space', 0)
    press_time('down', 4)
    press_time('right', 2)
    for i in range(4):
        sleep(0.05)
        press_time('right', 2)
    press_time('space', 0)
    press_time('right', 20)
    press_time('up', 1)

def level8():
    press_time('right', 12)
    press_time('up', 1)
    press_time('E', 0)
    press_time('space', 0)

    press_time('right', 8)
    press_time('up', 1)
    sleep(1)
    press_time('E', 0)
    press_time('space', 0)

    press_time('right', 5.1)
    press_time('up', 1)
    sleep(1.1)
    press_time('E', 0)
    press_time('space', 0)

    press_time('right', 2)
    press_time('up', 1)
    sleep(1.35)
    press_time('E', 0)
    press_time('left', 2)
    press_time('up', 4)

def level9():
    press_time('left', 4)
    press_time('up', 1)
    press_time('E', 0)
    sleep(1)
    press_time('E', 1)
    sleep(2)
    press_time('E', 0)
    press_time('space', 0)

    press_time('right', 4)
    press_time('up', 1)
    sleep(1)
    press_time('E', 0)
    sleep(2)
    press_time('E', 1)
    sleep(1)
    #press_time('E', 0)
    press_time('space', 0)

    press_time('up', 17)
    press_time('right', 4)
    press_time('up', 0)
    press_time('E', 0)

    press_time('left', 8)
    press_time('up', 0)
    press_time('E', 0)
    press_time('right', 4)
    press_time('up', 2)

def level10():
    press_time('up', 4)
    press_time('right', 2)
    for i in range(4):
        sleep(0.05)
        press_time('right', 2)
    press_time('space', 0)
    press_time('down', 4)
    press_time('right', 2)
    for i in range(4):
        sleep(0.05)
        press_time('right', 2)

    def go_to_m():
        press_time('space', 0)
        press_time('right', 19)
        sleep(0.2)
        press_time('right', 1)

    go_to_m()
    press_time('down', 3)
    go_to_m()
    press_time('right', 3)
    press_time('down', 3)
    go_to_m()
    press_time('right', 9)
    press_time('up', 1)
    press_time('E', 1)
    go_to_m()
    sleep(0.33)
    press_time('down', 6)
    press_time('left', 1)
    go_to_m()
    sleep(0.33)
    press_time('right', 3)
    press_time('down', 6)
    press_time('right', 1)
    press_time('space', 0)
    press_time('left', 1)
    press_time('down', 4)
    press_time('right', 1)
    sleep(4.7)
    press_time('up', 10)

def main():
    sleep(5)
    press_time('r', 10)
    #press_time('left', , 1)
    s = 2.5
    level1()
    sleep(s)
    level2()
    sleep(s)
    level3()
    sleep(s)
    level4()
    sleep(s)
    level5()
    sleep(s)
    level6()
    sleep(s)
    level7()
    sleep(s)
    level8()
    sleep(s)
    level9()
    sleep(s)
    level10()
    sleep(s)
    press_time('up', 10)
main()