import json
import psutil
from sysconfig import (get_platform)



# make sure that the system is windows
def v_platform():
    if ("win" not in get_platform()):
        raise Exception("Not supported OS. This only work in Windows.")



# make sure that CHR-RDP service is present
def v_chr_srvc():
    try:
        psutil.win_service_get('CHRRDP')

        return 1

    except psutil.NoSuchProcess as _:
        print("[ERROR (psutil.NoSuchProcess)] CHR-RDP service is not installed on this machine.")
        print("make sure that CHR-RDP application is installed.")

    return 0



"""
make sure that Wi-Fi interface is present and active.

0 is returned:
--- a. try to restart the network interface without a full system restart.
--- b. full system restart if needed

1 is returned:
--- a. try to connect to a network from the list.

-1 is returned:
the interface is on and connected to a Wi-Fi.
"""
def v_net_interface(verbose = False):
    addrs = psutil.net_if_addrs()

    if verbose:
        print(f"Detected Interfaces:\n{json.dumps(addrs, sort_keys=True, indent=4)}\n")

    # 1. check if the Wi-Fi key is present.
    # 2. check if it has private IP.

    if "Wi-Fi" not in addrs:
        return ("Wi-Fi interface is off. try to actiavte it or do a full restart.", 0, "N/A")
    
    c = len(addrs['Wi-Fi'])
    detected = False
    private_ip = "N/A"

    for i in range(c):
        if "192.168" in addrs['Wi-Fi'][i][1]: # TODO: read the private ip from config file.
            detected = True
            private_ip = addrs['Wi-Fi'][i][1]
            break


    if not detected:
        return ("Wi-Fi interface is on, but not connect to a Wi-Fi.", 1, "N/A")
    

    return ("Wi-Fi interface is on and connected to a Wi-Fi.", -1, private_ip)



# make sure that the current Wi-Fi is working and can reach to "https://gmail.com/".
# This can be done by using a simple ICMP ping. Also the ping will happen after connecting to Wi-Fi.
def v_net_ping():
    pass
