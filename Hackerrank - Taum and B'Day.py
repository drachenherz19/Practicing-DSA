def taumBday(b, w, bc, wc, z):
    # Write your code here
    money = 0
    
    if bc<wc+z:
        money += b*bc
    else:
        money += b*(wc+z)
        
    if wc<bc+z:
        money += w*wc
    else:
        money += w*(bc+z)