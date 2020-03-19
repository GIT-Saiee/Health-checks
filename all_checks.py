#!/usr/bin/env python3
import os
import sys
def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
#need to add a check_disk_full function
def main():
    if check_reboot():
        print("pending reboot")
        sys.exit(1)
    if check_disk_full(disk="/",min-gb= 2, min_percent=10):
        print("Disk full.")
    sys.exit(1)

main()
