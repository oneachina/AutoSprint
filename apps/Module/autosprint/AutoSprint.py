import keyboard
import threading
import time


class AutoSprint:
    def __init__(self):
        self.enable = True
        self.running = False
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while True:
            if self.enable and not self.running:
                self.running = True
                print("[info] AutoSprint Enabled")
                while self.enable:
                    if keyboard.is_pressed('w'):
                        keyboard.press('ctrl')
                        time.sleep(0.1)  # 适当的时间间隔
                        keyboard.release('ctrl')
                    time.sleep(0.01)  # 防止 CPU 占用过高
                self.running = False
                print("[info] AutoSprint Disabled")

    def toggle(self):
        self.enable = not self.enable

if __name__ == "__main__":
    sprint = AutoSprint()
    while True:
        if keyboard.is_pressed('I'):
            sprint.toggle()
            time.sleep(0.5)  # 防止多次触发
