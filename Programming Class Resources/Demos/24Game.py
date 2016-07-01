# The 24 Game Solver Python Version
# @author Xingfan Xia
import math

PRECISION = 1E-6
COUNT_OF_NUMBER = 4
NUMBER_TO_BE_CAL = 24
g_expression = []
g_number = []
#input
numInput = str(input('''enter the numbers you want to solve
Note: each number has to be separated by A SPACE
you can enter any numbers you like and any amount of it
'''))

#initialization
g_expression = numInput.split()
g_number = [0]*len(g_expression)
COUNT_OF_NUMBER = len(g_expression)
for i in range(len(g_expression)):
    g_number[i] = int(g_expression[i])

#recursive solver
def solve(n):
    if(1 == n):
        if(math.fabs(NUMBER_TO_BE_CAL - g_number[0]) < PRECISION):
            print("The answer is: " + g_expression[0] + " = 24")
            return True
        else:
            return False
    else:
        for i in range(0, n):
            for j in range(i+1, n):
                a = g_number[i]
                b = g_number[j]
                #**********************************
                #   Move the meaingful forward
                #   answer saved in [i]
                #   number[j]can just be overwritten by the last number
                #   *******************************
                g_number[j] = g_number[n - 1]
                expa = g_expression[i]
                expb = g_expression[j]
                g_expression[j] = g_expression[n - 1]
                # cal a+b
                g_expression[i] = '(' + expa + '+' + expb + ')'
                g_number[i] = a + b
                if ( solve(n - 1) ) :
                    return True

                # cal a-b
                g_expression[i] = '(' + expa + '-' + expb + ')'
                g_number[i] = a - b
                if ( solve(n - 1) ) :
                    return True

                # cal b-a
                g_expression[i] = '(' + expb + '-' + expa + ')'
                g_number[i] = b - a
                if ( solve(n - 1) ):
                    return True

                # cal (a*b)
                g_expression[i] = '(' + expa + '*' + expb + ')'
                g_number[i] = a * b
                if ( solve(n - 1) ):
                    return True

                # cal (a/b)
                if (b != 0) :
                    g_expression[i] = '(' + expa + '/' + expb + ')'
                    g_number[i] = a / b
                    if ( solve(n - 1) ) :
                        return True

                # cal (b/a)
                    if (a != 0) :
                        g_expression[i] = '(' + expb + '/' + expa + ')'
                        g_number[i] = b / a
                        if ( solve(n - 1) ):
                            return True

                 # resume and recursion
                g_number[i] = a
                g_number[j] = b
                g_expression[i] = expa
                g_expression[j] = expb
        return False
#main
if(not solve(COUNT_OF_NUMBER)):
    print('no solution')