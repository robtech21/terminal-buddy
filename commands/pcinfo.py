import psutil
import shutil

def get_cpu_temp():
    return psutil.sensors_temperatures()

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")

    print("Total: %d GiB" % (total // (2**30)))
    print("Used: %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))
    return total, used, free