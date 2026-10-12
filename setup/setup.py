import subprocess
import sys

def install_pip(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Installing required packages...")

install_pip("fastf1")

print("Installing fastf1...")

import fastf1

print("Enabling FastF1 cache...")

fastf1.Cache.enable_cache("setup/cache")

import logging

print("FastF1 cache enabled. Cache directory: cache")