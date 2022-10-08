def main(bi):
    pow = len(str(bi)) -1
    dec = 0
    for x in str(bi):
        dec += int(x)*(2**pow)
        pow -= 1 
    return dec
    
if __name__ == '__main__':
    print('Decimal eequivavlent :' , main(input('Binary number: ')))
