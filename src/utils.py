#!/usr/bin/env python

##
## EPITECH PROJECT, 2018
## 108trigo_2017
## File description:
## Utils file
##

from sys import exit, argv, stderr

def tab_fcts():
    fct_tab = [my_exp, my_cos, my_cosh, my_sinh]

def my_help():
    print("USAGE\n"
          "\t./108trigo fun a0 a1 a2....\n"
          "\n"
          "DESCRIPTION\n"
          "\tfun\tfunction to be applied,"
          ' among at least "EXP", "COS", "SIN", "COSH" and "SINH"\n'
          '\tai\tcoeficients of the matrix')
    exit(0)

def check_parameters():
    if "--help" in argv or "-h" in argv:
        my_help()
    if len(argv) <= 2 or argv[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        print("Bad format, see --help, -h, or man entry for more info", file=stderr)
        exit(84)
    try:
        for i in range(2, len(argv)):
            argv[i] = float(argv[i])
    except ValueError:
        print("Argument %d (%s) must be a number" % (i, argv[i]), file=stderr)

def error_mngmt():
    i = len(argv) - 2
    sqi = trunc(sqrt(i))
    if trunc(sqrt(i)) ** 2 != i:
        print("Not enough parameters to create a matrix", file=stderr)
        exit(84)
    return sqi

def print_matrix(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print("%.2f%c" % (tab[i][j], '\t' if (j != len(tab[i]) - 1) else '\n'), end="")

def launch_func(tab):
    args = ["EXP", "COS", "SIN", "COSH", "SINH"]
    fct_tab = [my_exp, my_cos, my_sin, my_cosh, my_sinh]
    for i in range(len(fct_tab)):
        if argv[1] == args[i]:
            tab = fct_tab[i](tab)
    return tab
