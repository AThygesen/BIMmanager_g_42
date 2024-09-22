# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Basis_a1 import spaces_amount
from Basis_2  import beam_length
from Basis_3  import wall_name
from Basis_4  import door
from Basis_6 import time_to_load

def print_hi(ifc_file):
    print('Amount of spaces', spaces_amount(ifc_file))
    print('Beam length', beam_length(ifc_file))
    print('Wall name', wall_name(ifc_file))
    print('')
ifc_file = ''
action = ''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(ifc_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
