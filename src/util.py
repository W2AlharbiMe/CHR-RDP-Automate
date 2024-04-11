import ctypes
from datetime import timedelta

# this will be used to restart the system based on "restart_system_when_uptime".
def uptime():
    lib = ctypes.windll.kernel32
    t = int(str(lib.GetTickCount64())[:-3]) 

    return timedelta(seconds=t)


"""
this will read and parse config.json.

--- config.json options ---

service_name:
the windows service name it should be "CHR-RDP".


main_wifi_target:
a wifi which have high priority before trying failover.


failover_wifi:
when the main_wifi_target fail to connect or it does not exists then try a wifi from the list.


log_file_path:
the place for a txt file that will have some logs that includes:
    - can not activate the Wi-Fi interface.
    - can not do a reboot.
    - Wi-Fi switching
    - Script Errors


verbose:
show more logs in console that might be helpful in debugging.


wait_time_for_wifi_switching:
when connecting to a Wi-Fi wait <int><str> time and switch to other Wi-Fi from failover.


restart_system_when_uptime:
when the system uptime is greater than or equal this value then restart.
if you are at the office the script will show a dialog, and you can choose if you want a restart or skip to next restart window.


try_main_wifi_count:
before trying to move to failover APs try to connect to main_wifi_target <int> times then try failover.

"""
def read_config(path = ""):
    pass



def parse_script_options(options):
    pass



def connect_to_wifi(name = ""):
    pass



def switch_wifi_after(wait_time = "3m"):
    pass



"""
before switching to a wifi show a dialog for <int><str> time to allow the user to control wether to switch or skip switch.
"""
def show_connection_dialog():
    pass



"""
restart windows and then run the script
"""
def reboot_system():
    pass



def enable_wifi_interface(interfaceName):
    pass



def enable_chr_rdp_service():
    pass



def run_application(name = "chr_rdp.bat"):
    pass
