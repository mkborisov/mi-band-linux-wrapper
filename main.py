import os, subprocess
import argparse
import time
from bluepy.btle import Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, ADDR_TYPE_PUBLIC, BTLEException
from subprocess import DEVNULL
from constants import CONST

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--model', required=True, choices=['3', '4'], help='Set model of the device')
parser.add_argument('-mac', '--mac', required=True, help='Set mac address of the device')
parser.add_argument('-j', '--jam', required=False, action='store_true', help='Jam device advertising, preventing other devices from connecting')
parser.add_argument('-k', '--authkey', required=False, help='Set device Auth Key (mi band 4 only)')
args = parser.parse_args()

if args.model:
    MI_BAND_MODEL = args.model
else:
    print("Error:")
    print("  Please specify the model of the MiBand")
    print("  Pass the --model option with the model")
    print("  Supported options: 3, 4")
    exit(1)

if args.mac:
    MAC_ADDR = args.mac
else:
    print("Error:")
    print("  Please specify MAC address of the MiBand")
    print("  Pass the --mac option with MAC address")
    print("  Example of MAC: FD:5F:8C:B0:BD:52")
    exit(1)

if args.authkey:
    AUTH_KEY = args.authkey
else:
    AUTH_KEY = CONST.DUMMY_AUTH_KEY

# callback class
class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, hnd, data):
        print(data)

class MiBandTestLib(Peripheral):
    def exec_python_script(self, band_model, mac_addr):

        if (band_model == '3'):
            self.proc = subprocess.run(["python", CONST.MIBAND3_MAIN_SCRIPT, mac_addr])
            self.process_response_handler(self.proc.returncode)
        elif (band_model == '4'):

            if (AUTH_KEY == CONST.DUMMY_AUTH_KEY):
                print("Warning: To use additional features on Mi Band 4, pass the --authkey option with your valid Auth Key")

            self.proc = subprocess.run(["python3", CONST.MIBAND4_MAIN_SCRIPT, "-m", mac_addr, "-k", AUTH_KEY])
            self.process_response_handler(self.proc.returncode)
        else:
            print("Please enter the Mi Band model. Possible options: 3, 4")
            return

        
    def process_response_handler(self, return_code):
        if (return_code == 0):
            print("Process executed successfully")
        else:
            print("Process could not execute properly. Exit code: %d" % return_code)
            exit(1)

    def query_ble_device_characteristics(self):
        if (MI_BAND_MODEL == '3'):
            self.addr_type = ADDR_TYPE_RANDOM
        elif (MI_BAND_MODEL == '4'):
            self.addr_type = ADDR_TYPE_PUBLIC
        else:
            return

        print("Advertise jamming for device with MAC: %s .To stop the process, press CTRL+C" % MAC_ADDR)

        self.command = "gatttool -b " + MAC_ADDR + " -t " + self.addr_type + " -i hci0 --char-read --handle 0x0003"

        while True:
            try:
                self.proc = subprocess.Popen(self.command, stdout=DEVNULL, shell=True)
                self.process_response_handler(self.proc.wait())

                time.sleep(1)

            except KeyboardInterrupt:
                print ('Stopping advertise jamming process')
                exit(0)

x = MiBandTestLib()

if args.jam:
    x.query_ble_device_characteristics()
else:
    x.exec_python_script(MI_BAND_MODEL, MAC_ADDR)

exit(0)