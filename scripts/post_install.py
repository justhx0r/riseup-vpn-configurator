import subprocess
import pprint
def main():
    pprint.pprint(subprocess.getoutput("riseup-vpn-configurator --install"))