import ifcopenshell
import time
import pandas as pd


def time_to_load(ifc_file):
    # starting time
    start = time.time()
    ifc_file = ifcopenshell.open(ifc_file)
    end = time.time()

    print()  # total time taken
    print(f"model load time is... {end - start}\n")