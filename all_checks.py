#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
def main():
    if check_reboot():
        print("pending reboot")
        sys.exit(1)
    if check_disk_full("/", 2, 10):
        print("Disk full.")
    sys.exit(1)

main()
