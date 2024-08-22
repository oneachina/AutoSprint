import keyboard


class AutoSprint:
    def enable(self):
        print("[info] AutoSprint Enable")
        keyboard.wait('w')
        keyboard.press('ctrl')
        keyboard.release('ctrl')

    def disabled(self):
       print("[info] AutoSprint Disabled")

