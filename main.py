from wmi import WMI
from os import system, name
from time import sleep


class App:
    def __init__(self):
        self.processor_name = WMI().Win32_Processor()[0].name
        self.gpu_name = WMI().Win32_VideoController()[0].name
        if name == "nt":
            system("color 0a")

    def run(self):
        system("systeminfo")
        print(f"PROCESSOR NAME: {self.processor_name}\nGPU NAME: {self.gpu_name}")
        sleep(True)


if __name__ == "__main__":
    app = App()
    app.run()
