number = 6011000000000004
new_number_list  =[2*int(val) if idx%2!=0 else int(val) for idx,val in enumerate(str(number)[::-1]) ]
new_number = "".join(map(str,new_number_list))
check_list = sum([int(i) for i in new_number])
print(check_list%10==0)


def valid_credit_card(number):
    new_number_list  =[2*int(val) if idx%2!=0 else int(val) for idx,val in enumerate(str(number)[::-1]) ]
    new_number = "".join(map(str,new_number_list))
    check_list = sum([int(i) for i in new_number])
    return check_list%10==0

def valid_credit_card2(n):
    n1=[ int( i ) for i in str( n) ][::-1]
    for i in range ( 1, len( n1 ), 2 ): n1[i ]= n1[i ] * 2
    n1=[ n1[i ] % 10 + n1[i ] // 10 if i % 2 else n1[i ] for i in range( len( n1 ) ) ]
    return sum(n1[1:]) * 9 % 10 == n%10