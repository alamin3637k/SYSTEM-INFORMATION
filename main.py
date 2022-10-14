from wmi import WMI
from subprocess import check_output
from os import system, name
from time import sleep


class App:
    def __init__(self):
        self.Id: list[str] = check_output(['systeminfo']).decode('utf-8').split('\n')
        self.new = []
        self.item = None
        self.i = None
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
