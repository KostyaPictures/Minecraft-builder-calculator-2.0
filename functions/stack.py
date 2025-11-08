def do(items):
    o_o=round(items-int(items),3)
    items=int(items)
    i=items%64
    items//=64
    s=items%27
    items//=27
    c=items%2
    items//=2
    dc=items

    res=""
    if dc!=0:
        res+=f"{dc} dc "
    if c!=0:
        res+=f"{c} c "
    if s!=0:
        res+=f"{s} s "
    if i!=0:
        res+=f"{i} i "
    if o_o!=0:
        res+=f"+ {o_o}"
    return res