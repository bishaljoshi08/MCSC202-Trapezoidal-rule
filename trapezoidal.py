from math import exp ,sin
from tabulate import tabulate


def single_integration(a,b,n,roun):
    h = ( a - b ) / n
    value = h*(f1(a) + f1(b))/2
    for i in range(1,n):
        value += h*f1(b + i * h)    
    value = round(value,roun)
    print ('The integration is %f' %value)

def choice_of_int():
    choice_of_integration = int(input('Enter 1 for single or 2 for double integration: '))
    if choice_of_integration == 1 :
        a = float(input('Enter the upper limit of integration: '))
        b = float(input('Enter the lower limit of integration: '))
        choice_of_subinterval_single(a,b)
    elif choice_of_integration == 2:
        a = float(input('Enter the upper limit of integration for x: '))
        b = float(input('Enter the lower limit of integration for x: '))
        c = float(input('Enter the upper limit of integration for y: '))
        d = float(input('Enter the lower limit of integration for y: '))
        choice_of_subinterval_double(a,b,c,d)
    else:
        print('You entered a wrong response!!')
        choice_of_int()
    
def choice_of_subinterval_single(a,b):
    choice_of_subinterval = int(input('Enter 1 if you have sub-interval 2 if you have difference: '))
    if choice_of_subinterval == 1:
        n = int(input('Enter the subinterval: '))
    elif choice_of_subinterval == 2:
        h = float(input('Enter the difference: '))
        n = int((a-b)/h) 
    else:
        print('You entered a wrong response!!')
        choice_of_subinterval_single(a,b)
    roun = int(input('Round up to how many digits: '))
    single_integration(a,b,n,roun)


def choice_of_subinterval_double(a,b,c,d):
    choice_of_subinterval = int(input('Enter 1 if you have sub-interval 2 if you have difference: '))
    if choice_of_subinterval == 1:
        nx = int(input('Enter the subinterval for x: '))
        ny = int(input('Enter the subinterval for y: '))
    elif choice_of_subinterval == 2:
        h = float(input('Enter the difference for x: '))
        k = float(input('Enter the difference for y: '))
        nx = int((a-b)/h)
        ny = int((c-d)/k)
    else:
        print('You entered a wrong response!!')
        choice_of_subinterval_double(a,b,c,d)
    roun = int(input('Round up to how many digits: '))
    double_integration(a,b,c,d,nx,ny,roun)



def f1(x):
    return 2**x


def f(x,y):
    return exp(x+y)

def double_integration(a,b,c,d,nx,ny,roun):
    h = (a-b)/nx
    k = (c-d)/ny
    multable = [[2 for i in range(nx+2)] for j in range(ny+2)]
    multable[0][0] = 'X'
    multable[1][0] = multable[0][1] = multable[0][nx+1] = multable[ny+1][0] = 1 

    # multable = [['X',1,4,2,4,1],
    # [1,0,0,0,0,0],
    # [4,0,0,0,0,0],
    # [2,0,0,0,0,0],
    # [4,0,0,0,0,0],
    # [1,0,0,0,0,0],
    # ]

    for i in range(1,ny+2):
        for j in range (1,nx+2):
            multable[i][j] = multable[i][0] * multable[0][j]
    print('The multiplication table is:')
    # for row in multable:
    #     x.rows.append(row)
    print(tabulate(multable))
    print('*'*100)

    fuction_table = [[0 for i in range(nx+2)] for j in range(ny+2)]
    fuction_table[0][0] = 'f(x,y)'
    for i in range(1,ny+2):
        fuction_table[i][0] = d + (i-1)*h
    for i in range(1,nx+2):
        fuction_table[0][i] = b + (i-1)*k

    for i in range(1,ny+2):
        for j in range (1,nx+2):
            fuction_table[i][j] = round(f(fuction_table[0][j] ,fuction_table[i][0]),roun)
    
    print('The functional table is:')
    # for row in fuction_table:
    #     y.rows.append(row)
    print(tabulate(fuction_table))
    print('*'*100)

    value = 0.0
    for i in range(1,ny+2):
        for j in range (1,nx+2):
            value += (fuction_table[i][j] * multable[i][j])

    value = round((h*k*0.25*value),roun)
    # value = round((h*(k/9)*value),roun)

    print (f'The integration value is {value:f}' )

# x = BeautifulTable()
# x.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
# y = BeautifulTable()
# y.set_style(BeautifulTable.STYLE_BOX_ROUNDED)


choice_of_int()








