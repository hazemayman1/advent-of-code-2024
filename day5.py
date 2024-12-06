
############## DAY 5 PART1  ##############

def count_correct(file):
    inputs, rules = read_input(file=file)
    correct_rows = []
    for line in inputs:
        correct_line = True
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                if rules.get(line[i]):
                    if line[j] in rules[line[i]]:
                        correct_line = False 
                        break
            if correct_line == False:
                break
        if correct_line:
            correct_rows.append(line)
    return correct_rows



def read_input(file):
    f = open(file, 'r')
    rules = {}
    inputs = []
    split = False
    for line in f:
        if not line.strip():
            split = True
            continue
        if split:
            inputs.append(list(map(int, line.split(','))))
        else:
            rule_key = int(line[3:])
            rule_value = int(line[:2])
            if not rules.get(rule_key):
                rules[rule_key] = []
                rules[rule_key].append(rule_value)
            else:
                rules[rule_key].append(rule_value)
    return inputs, rules

def sum_middle_elements(lists):
    sum = 0
    for list in lists:
        sum += list[len(list) // 2]
    print(sum)

rows = count_correct("mini_input day5.txt")
sum_middle_elements(rows)

##PART 2 ADJUSTMENT 

def count_correct(file):
    inputs, rules = read_input(file=file)
    correct_rows = []
    for line in inputs:
        correct_line = True
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                if rules.get(line[i]):
                    if line[j] in rules[line[i]]:
                        temp = line[j]
                        line[j] = line[i]
                        line[i] = temp 
                        correct_line = False
        if not correct_line:
            correct_rows.append(line)
    return correct_rows

