def main(dec):
    import math as mth
    
    
    n1 = int(dec)
    bi = ''
    while n1 > 0:
        bi += str(n1 % 2)
        n1 = mth.floor(n1 / 2)
    return(bi[::-1])

    
if __name__ == '__main__':
    print('Binary eequivavlent :' , main(input('Decimal number: ')))
