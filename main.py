##
## EPITECH PROJECT, 2018
## 108trigo_2017
## File description:
## Main function
##

import sys
from utils import *

def main():
    tab = []
    check_parameters()
    sqi = error_mngmt()
    for i in range(int(sqi)):
        tab.append([])
        for j in range(int(sqi)):
            tab[i].append(sys.argv[i * int(sqi) + j + 2])
    tab = launch_func(tab)
    print_matrix(tab)
