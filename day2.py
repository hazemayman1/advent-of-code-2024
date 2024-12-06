

####################### DAY2 ####################

reps = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]

def is_safe(rep):
    ptr1 = 0
    ptr2 = 1
    inc = True
    correct = True
    failed_indx1 = -1
    failed_indx2 = -1
    if rep[ptr1] > rep[len(rep) -1]:
        inc = False
    if inc:
        while ptr2 != len(rep):
            diff = rep[ptr2] - rep[ptr1]
            if not 1 <= diff <= 3:
                correct = False
                failed_indx1 = ptr1
                failed_indx2 = ptr2
                break
            ptr1 += 1
            ptr2 += 1
    else:
        while ptr2 != len(rep):
            diff = rep[ptr1] - rep[ptr2] 
            if not 1 <= diff <= 3:
                correct = False
                failed_indx1 = ptr1
                failed_indx2 = ptr2
                break
            ptr1 += 1
            ptr2 += 1
    return correct, failed_indx1, failed_indx2

def count_safe_reports(reps):
    safe = 0
    for rep in reps:
        correct, failed_indx1, failed_indx2 = is_safe(rep)
        if not correct:
            correct1, _, _ = is_safe(rep[:failed_indx1] + rep[failed_indx1+1:])
            correct2, _, _ = is_safe(rep[:failed_indx2] + rep[failed_indx2+1:])
            correct = correct1 or correct2
        online_correct = online_is_really_safe(rep)
        print(correct, online_correct, rep, rep[:failed_indx1] + rep[failed_indx1+1:], rep[:failed_indx2] + rep[failed_indx2+1:]) if correct != online_correct else ""
        if correct:
            safe += 1
    return safe

f = open('input.txt', 'r')

def online_is_safe(nums):
    inc = nums[1] > nums[0]
    if inc:
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if not 1<= diff <= 3:
                return False
        return True
    else:
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if not -3<= diff <= -1:
                return False
        return True

def online_is_really_safe(nums):
    if online_is_safe(nums):
        return True
    for i in range(len(nums)):
        if online_is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

l1 = []
l2 = []
for line in f:
    l1.append([int(item) for item in line.split()])  
# print(l1)

reps = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
[1, 4 ,3 ,4, 5],
[1,2,1]
]

# print(online_is_safe(reps))

# print(count_safe_reports(reps))

