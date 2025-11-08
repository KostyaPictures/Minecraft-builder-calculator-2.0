from operator import length_hint

import functions.json_ops as json_ops
import functions.stack as stack
from math import floor, ceil
import re

def calc(number, from_, to_, path):
    print(number, from_, "to ", to_)
    try:
        number=float(number)
    except (TypeError, ValueError):
        return ""
    vfrom=json_ops.get_values(from_, path)
    print(vfrom)
    vto=json_ops.get_values(to_, path)
    print(vto)
    dont_rnd=json_ops.get_rnd(path)
    e1=number/vfrom[1]
    if not dont_rnd:
        e1=ceil(e1)
    e2=e1*vfrom[0]/vto[0]
    if not dont_rnd:
        e2=floor(e2)

    res=e2*vto[1] #(number/vfrom[1]*vfrom[0])/vto[0]*vto[1]

    if json_ops.get_logs(path):
        res=ceil(res/4)

    if dont_rnd:
        res=round(res,3)

    if json_ops.get_stack(path):
        res=stack.do(res)

    return str(res)


def calc_to_int(str_):
    str_old=str_
    parts = re.split(r'(\d+)', str_)
    splited = [int(part) if part.isdigit() else part for part in parts if part]
    #[15, '*', 16, '+', 45, '/', 1343, '/', 59]
    res=0
    i=0
    print(splited)
    try:
        res=splited[i]
        for n in splited:
            #if i.isdigit():
            #    res=i
            if n=="*":
                res*=splited[i+1]
            if n=="/":
                res/=splited[i+1]
            if n=="+":
                res+=splited[i+1]
            if n=="-":
                res-=splited[i+1]
            i+=1
        return float(res)
    except (TypeError, IndexError):
        return str_old




#print(calc_to_int("10+16/"))