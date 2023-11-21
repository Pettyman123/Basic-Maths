def largest_nt_factor( interesting_int ):
    factor = 2

    while interesting_int  % factor != 0:
        factor += 1

    if  factor == interesting_int :
        return -1
    else:
        return interesting_int // factor 

print( largest_nt_factor( 101 ))