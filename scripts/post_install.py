import subprocess
def main():
    subprocess.run(["/usr/local/bin/riseup-vpn-configurator","--install"])
    subprocess.run(["/usr/local/bin/riseup-vpn-configurator","--service-mode"])