from tabulate import tabulate
from Equation import Expression


def single_integration(a,b,n,roun):
    exp = input('Enter the expression in term of x: ')
    f1 = Expression(exp, ["x"])
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
        roun = int(input('Round up to how many digits: '))
        choice_of_subinterval_single(a,b,roun)
    elif choice_of_integration == 2:
        a = float(input('Enter the upper limit of integration for x: '))
        b = float(input('Enter the lower limit of integration for x: '))
        c = float(input('Enter the upper limit of integration for y: '))
        d = float(input('Enter the lower limit of integration for y: '))
        roun = int(input('Round up to how many digits: '))
        choice_of_subinterval_double(a,b,c,d,roun)
    else:
        print('You entered a wrong response!!')
        choice_of_int()
    
def choice_of_subinterval_single(a,b,roun):
    choice_of_subinterval = int(input('Enter 1 if you have sub-interval 2 if you have difference: '))
    if choice_of_subinterval == 1:
        n = int(input('Enter the subinterval: '))
    elif choice_of_subinterval == 2:
        h = float(input('Enter the difference: '))
        n = int(round((a-b)/h,roun)) 
    else:
        print('You entered a wrong response!!')
        choice_of_subinterval_single(a,b,roun)
    single_integration(a,b,n,roun)


def choice_of_subinterval_double(a,b,c,d,roun):
    choice_of_subinterval = int(input('Enter 1 if you have sub-interval 2 if you have difference: '))
    if choice_of_subinterval == 1:
        nx = int(input('Enter the subinterval for x: '))
        ny = int(input('Enter the subinterval for y: '))
    elif choice_of_subinterval == 2:
        h = float(input('Enter the difference for x: '))
        k = float(input('Enter the difference for y: '))
        nx = int(round((a-b)/h,roun))
        ny = int(round((c-d)/k,roun))
    else:
        print('You entered a wrong response!!')
        choice_of_subinterval_double(a,b,c,d,roun)
    
    double_integration(a,b,c,d,nx,ny,roun)
    

def double_integration(a,b,c,d,nx,ny,roun):
    exp = input('Enter the expression in terms of x and y: ')
    f = Expression(exp, ["x","y"])
    h = (a-b)/nx
    k = (c-d)/ny
    multable = [[2 for i in range(nx+2)] for j in range(ny+2)]
    multable[0][0] = 'X'
    multable[1][0] = multable[0][1] = multable[0][nx+1] = multable[ny+1][0] = 1 


    for i in range(1,ny+2):
        for j in range (1,nx+2):
            multable[i][j] = multable[i][0] * multable[0][j]
    print('The multiplication table is:')

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
    print(tabulate(fuction_table))
    print('*'*100)

    value = 0.0
    for i in range(1,ny+2):
        for j in range (1,nx+2):
            value += (fuction_table[i][j] * multable[i][j])

    value = round((h*k*0.25*value),roun)


    print (f'The integration value is {value:f}' )


choice_of_int()








