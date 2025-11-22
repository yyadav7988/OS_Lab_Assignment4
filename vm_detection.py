import platform
import subprocess

def detect_vm():
    try:
        output = subprocess.check_output("lscpu", shell=True).decode()
        if "Virtualization" in output:
            print("Likely running inside a virtual machine.")
        else:
            print("Physical machine or virtualization undetected.")
    except Exception as e:
        print("Unable to detect virtualization:", e)

print("=== VM Detection ===")
print("OS Info:", platform.system(), platform.release())
detect_vm()
