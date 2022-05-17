#!/usr/bin/python3

from random import random, uniform
import math

# ------------------------------
# Parâmetros
# ------------------------------

# Módulo de young Pa
import numpy as np
from colorama import Fore, Style, Back
from termcolor import cprint
from scipy.optimize import minimize

E = 200000000
# Módulo de corte GPa
G = 75.8
# Força Aplicada Kg
F = 2722
# Comprimento viga m
L = 0.3556
# Custo de material viga €/m3
custo_viga = 2935
# Custo de material soldadura €/m3
custo_soldadura = 67413


def get_inercia(t, b):
    if t == b:
        I = (b ** 4) / 12
    elif t > b:
        I = (b * (t ** 3)) / 12
    elif t < b:
        I = (t * (b ** 3)) / 12
    return I


def get_flecha_maxima(I):
    y = -F * (L ** 2) / (6 * E * I)
    return y


def custototal(t, b, l, h):

    viga = ((l + L) * t * b) * custo_viga
    solda = (l * h) * custo_soldadura
    custototal = viga + solda

    return custototal


def restricao1(b, l, h):

    alfa = math.atan(h / b)
    tensao_normal = (F * math.sin(alfa)) / (h * l)

    if tensao_normal > 200000:
        restricao1_valida = False
        cprint(f"Restrição 1 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao1_valida = True
        cprint(f"Restrição 1 valida", color='white', on_color='on_green', attrs=['bold'])

    return tensao_normal


def restricao2(b, l, h):

    alfa = math.atan(h / b)
    tensao_corte = (F * math.cos(alfa)) / (h * l)

    if tensao_corte > 90000:
        restricao2_valida = False
        cprint(f"Restrição 2 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao2_valida = True
        cprint(f"Restrição 2 valida", color='white', on_color='on_green', attrs=['bold'])

    return tensao_corte


def restricao3(flecha):
    if flecha > 0.0065:
        restricao3_valida = False
        cprint(f"Restrição 3 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao3_valida = True
        cprint(f"Restrição 3 valida", color='white', on_color='on_green', attrs=['bold'])


def restricao4(h):

    if h > 0.127:
        restricao4_valida = False
        cprint(f"Restrição 4 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao4_valida = True
        cprint(f"Restrição 4 valida", color='white', on_color='on_green', attrs=['bold'])
    return h


def restricao5(b):

    if b > 0.0032:
        restricao5_valida = False
        cprint(f"Restrição 5 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao5_valida = True
        cprint(f"Restrição 5 valida", color='white', on_color='on_green', attrs=['bold'])
    return b


def restricao6(l):

    if l > 0.254:
        restricao6_valida = False
        cprint(f"Restrição 6 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao6_valida = True
        cprint(f"Restrição 6 valida", color='white', on_color='on_green', attrs=['bold'])
    return l


def restricao7(t):

    if t > 0.0025:
        restricao7_valida = False
        cprint(f"Restrição 7 invalida", color='white', on_color='on_red', attrs=['bold'])
    else:
        restricao7_valida = True
        cprint(f"Restrição 7 valida", color='white', on_color='on_green', attrs=['bold'])
    return t


def fObjetivo(flecha, custo):
    funcao_objetivo = (0.5) * flecha + 0.5 * custo
    return funcao_objetivo


def main():
    t = random()
    b = random()
    l = random()
    h = random()
    Inercia = get_inercia(t, b)
    flecha = get_flecha_maxima(Inercia)
    custo = custototal(t, b, l, h)
    # print('Os valores de entrada são : ')
    # print(Back.BLACK + Fore.WHITE + 't = ' + str(t) + Style.RESET_ALL)
    # print(Back.BLACK + Fore.WHITE + 'b = ' + str(t) + Style.RESET_ALL)
    # print(Back.BLACK + Fore.WHITE + 'l = ' + str(t) + Style.RESET_ALL)
    # print(Back.BLACK + Fore.WHITE + 'h = ' + str(t) + Style.RESET_ALL)
    restricao1(b, l, h)
    restricao2(b, l, h)
    restricao3(flecha)
    restricao4(h)
    restricao5(b)
    restricao6(l)
    restricao7(t)
    result = fObjetivo(flecha, custo)
    cprint(f"Resultado da função objetivo {result}  ", color='white', on_color='on_blue', attrs=['bold'])


if __name__ == '__main__':
    main()
