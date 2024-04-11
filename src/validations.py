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


# make sure that Wi-Fi interface is present and active.
def v_net_interface():
    pass


# make sure that the current Wi-Fi is working and can reach to "https://gmail.com/".
# This can be done by using a simple ICMP ping. Also the ping will happen after connecting to Wi-Fi.
def v_net_ping():
    pass
