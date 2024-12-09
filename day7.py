from itertools import product

def verify_equation(list, result):
    operator_combinations = product(['+', '*', '||'], repeat=len(list) - 1)
    for op in operator_combinations:
        expr_list = []
        for a, b in zip(list, op):
            expr_list.extend([a, b])
        expr_list.extend(list[len(op):])
        evaluated_res = expr_list[0]
        i, j = 1,2
        while j <= (len(expr_list) - 1):
            if expr_list[i] == '*':
                evaluated_res *= expr_list[j]
            elif expr_list[i] == '+' :
                evaluated_res += expr_list[j]
            elif expr_list[i] == '||':
                evaluated_res = int(str(evaluated_res) + str(expr_list[j])) 
            i += 2
            j += 2
        if evaluated_res == result:
            return evaluated_res
    return 0



f = open('input day 7.txt', 'r')
list = []
for line in f:
    list.append([int(item.replace(':','')) for item in line.split()])  

final_sum = 0
for i in range(len(list)):
    final_sum += verify_equation(list[i][1:], list[i][0])
print(final_sum)
