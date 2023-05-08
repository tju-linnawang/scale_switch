# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:28:17 2023

@author: 25692
"""
#num为待转换字符串
#十进制整数转二进制
def dec_to_bin(num):
    l = [] 
    num = int(num)
    if num < 0:
        return "-" + dec_to_bin(abs()) 
    while True:
        num, reminder = divmod(num,2) 
        l.append(str(reminder)) 
        if num == 0: 
            return "".join(l[::-1])
#十进制转十六进制
def dec_to_hex(num):
    base = [str(x) for x in range(10)] +[chr(x) for x in range(ord('A'),ord("A")+6)]
    l = []
    num = int(num)
    if num < 0:
        return "-"+dec_to_hex(abs(num))
    while True:
        num,rem = divmod(num,16)
        l.append(base[rem])
        if num == 0:
            return "".join(l[::-1])
#二进制转换为十进制
def bin_to_dec(num):
    dec = 0
    power = 0
    num = int(num)
    while num > 0:
        dec += 2 ** power * (num % 10)
        num //= 10
        power += 1
    return dec
#二进制转换为十六进制
def bin_to_hex(num):
    return dec_to_hex(bin_to_dec(num))
#十六进制转换为二进制
def hex_to_bin(num):
    return dec_to_bin(hex_to_dec(num.upper()))
#十六进制转化为十进制
def hex_to_dec(num):
    return str(int(num.upper(),16))

