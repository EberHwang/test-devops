import os
import subprocess
import platform
import time

SECONDS_TO_DAYS = 1 / 86400

def check_for_updates():
    try:
        # Run the softwareupdate command to check for updates
        subprocess.run(['/usr/sbin/softwareupdate', '--list'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error checking for updates: {e}")

def install_updates():
    try:
        # Run the softwareupdate command to install updates
        subprocess.run(['/usr/sbin/softwareupdate', '-i -a -R'], check=True)
        print("Updates installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing updates: {e}")


if __name__ == "__main__":
    reboot = False;
    
    # Check system uptime
    uptime_days = time.monotonic() * SECONDS_TO_DAYS
    print(f'uptime: {uptime_days} days')
    if (uptime_days > 10):
        reboot = True
    
    version, _, architecture = platform.mac_ver()
    print(f'version: {version}')
    print(f'architecture: {architecture}')
    
    if int(version.split('.')[0]) < 15:
        check_for_updates()
        install_updates()
        reboot = True
    
    if reboot:
        # Reboot system after updates and packages
        os.system("shutdown -r now")
